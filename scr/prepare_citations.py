import csv
import gzip
from pathlib import Path


INPUT_FILE = Path("data/raw/cit-Patents.txt.gz")
OUTPUT_FILE = Path("data/neo4j-import/patent_citations_5000.csv")
RECORD_LIMIT = 5000


def prepare_citation_data():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    record_count = 0
    patent_ids = set()

    with gzip.open(INPUT_FILE, mode="rt", encoding="utf-8") as source_file:
        with OUTPUT_FILE.open(mode="w", newline="", encoding="utf-8") as output_file:
            writer = csv.writer(output_file)

            writer.writerow(["citing_patent", "cited_patent"])

            for line in source_file:
                line = line.strip()

                # Ignore empty lines and SNAP metadata headers
                if not line or line.startswith("#"):
                    continue

                values = line.split()

                if len(values) != 2:
                    continue

                citing_patent, cited_patent = values

                writer.writerow([citing_patent, cited_patent])

                patent_ids.add(citing_patent)
                patent_ids.add(cited_patent)

                record_count += 1

                if record_count == RECORD_LIMIT:
                    break

    print("Dataset preparation completed")
    print(f"Citation relationships: {record_count}")
    print(f"Unique patent nodes: {len(patent_ids)}")
    print(f"Output file: {OUTPUT_FILE}")


if __name__ == "__main__":
    prepare_citation_data()