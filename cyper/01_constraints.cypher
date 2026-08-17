CREATE CONSTRAINT patent_id_unique IF NOT EXISTS
FOR (p:Patent)
REQUIRE p.patent_id IS UNIQUE;