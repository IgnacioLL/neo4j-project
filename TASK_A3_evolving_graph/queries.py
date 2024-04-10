create_relation_rewiews ="""
LOAD CSV WITH HEADERS FROM 'file:///reviews_data.csv' AS row
MATCH (a:Author {author_id: row.author_id})
MATCH (p:Paper {id: row.id})
CREATE (a)-[:REVIEWD {approved: row.approved}]->(p);
"""

set_approved = """
MATCH (p)<-[r:REVIEWD]-()
WITH p, COUNT(r) AS TotalR
MATCH (p)<-[r:REVIEWD]-()
WHERE r.approved = "Yes"
WITH p, COUNT(r) AS NumberOfApprovals, TotalR
SET p.accepted = CASE WHEN NumberOfApprovals * 1.0 / TotalR > 0.5 THEN 'Yes' ELSE 'No' END
"""


create_relation_affiliation ="""
LOAD CSV WITH HEADERS FROM 'file:///affiliation_data.csv' AS row
MATCH (a:Author {author_id: row.author_id})
MERGE (s:School {name: row.school})
CREATE (a)-[:AFFILIATED_WITH]->(s);
"""
