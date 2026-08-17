LOAD CSV WITH HEADERS
FROM 'file:///patent_citations_5000.csv' AS row

MERGE (citing:Patent {
    patent_id: row.citing_patent
})

MERGE (cited:Patent {
    patent_id: row.cited_patent
})

MERGE (citing)-[:CITES]->(cited);