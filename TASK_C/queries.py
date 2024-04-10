load_communities ="""
LOAD CSV WITH HEADERS FROM 'file:///communities_data.csv' AS row
CREATE (co:Communities { 
    article_id: row.id,
    category: row.category
});
"""

create_relation_paper_community = """
MATCH (p:Paper), (co:Communities)
WHERE p.id = co.article_id
CREATE (p)-[:TOPIC]->(co);
"""