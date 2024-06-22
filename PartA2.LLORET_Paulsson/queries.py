# from config import BASE_URL
BASE_URL = "file:///temporal_zone/data/"

load_authors = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}authors_data.csv' AS row
CREATE (a:Author {{ 
    name: row.name,
    cleaned_name: row.cleaned_name,
    author_id: row.author_id,
    email: row.email
}})
"""

load_article = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}article_data.csv' AS row
CREATE (p:Paper {{ 
    year: row.year,
    id: row.id,
    title: COALESCE(row.title, ''),
    url: row.url,
    volume: row.volume,
    author_name: row.author_name,
    conference_edition: row.edition
}})
"""



create_relation_authors_article = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}article_authors_relation.csv' AS row
MATCH (a:Author {{author_id: row.author_id}})
MATCH (p:Paper {{id: row.article_id}})
CREATE (a)-[:AUTHORED]->(p)
"""

load_journals = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}article_data.csv' AS row
WITH DISTINCT row.journal AS journal
CREATE (j:Journal {{ name: journal }})
"""

create_relation_paper_journal = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}article_data.csv' AS row
MATCH (p:Paper {{ id: row.id }})
MATCH (j:Journal)
WHERE j.name = row.journal
CREATE (p)-[:PUBLISHED_IN]->(j)
"""


create_relation_year_journal = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}article_data.csv' AS row
MATCH (j:Journal {{ name: row.journal }})
MATCH (y:Year {{ year: row.year }})
CREATE (j)-[:OCCURRED_DURING]->(y)
"""

create_citations_data = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}citations_data.csv' AS row
WITH row
MATCH (p1:Paper {{ id: row.id }})
MATCH (p2:Paper {{ id: row.id_cited }})
CREATE (p1)-[:CITES]->(p2)
"""

load_conference = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}conference_data.csv' AS row
CREATE (:Conference {{name: row.conference_name}})
"""

load_city = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}city_data.csv' AS row
CREATE (:City {{name: row.city}})
"""

load_time = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}time.csv' AS row
CREATE (:Year {{year: toInteger(row.year)}})
"""

load_edition = f"""
LOAD CSV WITH HEADERS FROM '{BASE_URL}edition_data.csv' AS row
MERGE (edition:Edition {{conference_edition: row.conference_edition}})
MERGE (conference:Conference {{name: row.conference_name}})
MERGE (city:City {{name: Coalesce(row.city, 'Unknown')}})
MERGE (year:Year {{year: toInteger(row.year)}})
CREATE (edition)-[:HELD_IN]->(city)
CREATE (edition)-[:IN_YEAR]->(year)
CREATE (conference)-[:HAS_EDITION]->(edition)
"""


create_relation_paper_edition = f"""
MATCH (p:Paper), (e:Edition)
WHERE p.conference_edition = e.conference_edition
CREATE (p)-[:PRESENTED_IN]->(e)
"""


create_index_author= "CREATE INDEX authorNameIndex FOR (a:Author) ON (a.author_id)"
create_index_paper = "CREATE INDEX paperIdIndex FOR (p:Paper) ON (p.id)"