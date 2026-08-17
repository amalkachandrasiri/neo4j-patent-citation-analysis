// Query 1: Find all direct neighbours of a selected patent

MATCH (target:Patent {patent_id: "3858241"})
      -[citation:CITES]-
      (neighbor:Patent)

RETURN target, citation, neighbor;

// Query 1B: Direct-neighbour execution profile
PROFILE
MATCH (target:Patent {patent_id: "3858241"})
      -[citation:CITES]-
      (neighbor:Patent)
RETURN target.patent_id AS target_patent,
       neighbor.patent_id AS direct_neighbor;