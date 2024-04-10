load_authors = """
LOAD CSV WITH HEADERS FROM 'file:///authors_data.csv' AS row
CREATE (a:Author { 
    name: row.name,
    cleaned_name: row.cleaned_name,
    email: row.email
});
"""

load_article = """
LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
CREATE (p:Paper { 
    year: row.year,
    id: row.id,
    title: COALESCE(row.title, ''),
    url: row.url,
    volume: row.volume,
    author_name: row.author_name
});
"""


create_relation_authors_article ="""
LOAD CSV WITH HEADERS FROM 'file:///article_authors_relation.csv' AS row
MATCH (a:Author {id: row.author_id})
MATCH (p:Paper {id: row.paper_id})
CREATE (a)-[:AUTHORED]->(p);
"""


load_time = """
// import time
LOAD CSV WITH HEADERS FROM 'file:///time.csv' AS row
MERGE (y:Year { year: row.year });
"""


load_journals = """
// Import Journals
LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
WITH DISTINCT row.journal AS journal
MERGE (j:Journal { name: journal });
"""


load_cities = """
// Import Cities
LOAD CSV WITH HEADERS FROM 'file:///city_data.csv' AS row
MERGE (ct:City { name: row.city });
"""


load_conference_name = """
// Import Conferences
LOAD CSV WITH HEADERS FROM 'file:///conference_data.csv' AS row
WITH row WHERE row.conference_name IS NOT NULL
MERGE (c:Conference { conference_name: row.conference_name })
SET c.name = COALESCE(row.conference_name, '');
"""


load_conference_edition = """
// Import Conference Editions
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
MERGE (e:Edition { name: row.conference_edition })
SET e.city = row.city;
"""

create_conference_edition_relation = """
// Create Relationships between Conf and Edition
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
MATCH (c:Conference { name: row.conference_name })
MATCH (e:Edition { name: row.conference_edition, city: row.city })
CREATE (c)-[:HAS_EDITION]->(e);
"""


create_city_edition_relation = """
// Create Relationships between Conferences and Cities
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
MATCH (c:Conference { name: row.conference_name })
MATCH (ct:City { name: row.city })
MERGE (c)-[:HELD_IN]->(ct);
"""


create_relation_paper_journal = """
// Create relationship between Paper and Journal
LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
MATCH (p:Paper { id: row.id })
MATCH (j:Journal)
WHERE j.name = row.journal
MERGE (p)-[:PUBLISHED_IN]->(j);
"""


create_relation_year_journal = """// Create relationship between year and journal
LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
MATCH (j:Journal { name: row.journal })
MATCH (y:Year { year: row.year })
MERGE (j)-[:OCCURRED_DURING]->(y);
"""

create_citations_data = """LOAD CSV WITH HEADERS FROM 'file:///citations_data.csv' AS row
WITH row
MATCH (p1:Paper { id: row.id })
MATCH (p2:Paper { id: row.id_cited })
MERGE (p1)-[:CITES]->(p2);
"""


load_communities = """// Create Community nodes
LOAD CSV WITH HEADERS FROM 'file:///communities_data.csv' AS row
MERGE (c:Community { category: row.category });
"""


create_relation_paper_community = """// Create relationship between Paper and Community
LOAD CSV WITH HEADERS FROM 'file:///communities_data.csv' AS row
MATCH (p:Paper { id: row.id })
MATCH (c:Community { category: row.category })
MERGE (p)-[:HAS_TOPIC]->(c);
"""