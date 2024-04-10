load_authors = """
LOAD CSV WITH HEADERS FROM 'file:///authors_data.csv' AS row
CREATE (a:Author { 
    name: row.name,
    cleaned_name: row.cleaned_name,
    author_id: row.author_id,
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



create_index_author= "CREATE INDEX authorNameIndex FOR (a:Author) ON (a.author_id);"
create_index_paper = "CREATE INDEX paperIdIndex FOR (p:Paper) ON (p.id);"

create_relation_authors_article ="""
LOAD CSV WITH HEADERS FROM 'file:///article_authors_relation.csv' AS row
MATCH (a:Author {author_id: row.author_id})
MATCH (p:Paper {id: row.article_id})
CREATE (a)-[:AUTHORED]->(p);
"""


load_time = """
LOAD CSV WITH HEADERS FROM 'file:///time.csv' AS row
CREATE (y:Year { year: row.year });
"""


load_journals = """
LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
WITH DISTINCT row.journal AS journal
CREATE (j:Journal { name: journal });
"""


load_cities = """
LOAD CSV WITH HEADERS FROM 'file:///city_data.csv' AS row
CREATE (ct:City { name: row.city });
"""


load_conference_name = """
LOAD CSV WITH HEADERS FROM 'file:///conference_data.csv' AS row
WITH row WHERE row.conference_name IS NOT NULL
CREATE (c:Conference { conference_name: row.conference_name })
SET c.name = COALESCE(row.conference_name, '');
"""


load_conference_edition = """
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
CREATE (e:Edition { name: row.conference_edition })
SET e.city = row.city;
"""

create_conference_edition_relation = """
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
MATCH (c:Conference { name: row.conference_name })
MATCH (e:Edition { name: row.conference_edition, city: row.city })
CREATE (c)-[:HAS_EDITION]->(e);
"""


create_city_edition_relation = """
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
MATCH (c:Conference { name: row.conference_name })
MATCH (ct:City { name: row.city })
CREATE (c)-[:HELD_IN]->(ct);
"""


create_relation_paper_journal = """
LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
MATCH (p:Paper { id: row.id })
MATCH (j:Journal)
WHERE j.name = row.journal
CREATE (p)-[:PUBLISHED_IN]->(j);
"""


create_relation_year_journal = """
LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
MATCH (j:Journal { name: row.journal })
MATCH (y:Year { year: row.year })
CREATE (j)-[:OCCURRED_DURING]->(y);
"""

create_citations_data = """
LOAD CSV WITH HEADERS FROM 'file:///citations_data.csv' AS row
WITH row
MATCH (p1:Paper { id: row.id })
MATCH (p2:Paper { id: row.id_cited })
CREATE (p1)-[:CITES]->(p2);
"""


load_communities = """
LOAD CSV WITH HEADERS FROM 'file:///communities_data.csv' AS row
CREATE (c:Community { category: row.category });
"""


create_relation_paper_community = """
LOAD CSV WITH HEADERS FROM 'file:///communities_data.csv' AS row
MATCH (p:Paper { id: row.id })
MATCH (c:Community { category: row.category })
CREATE (p)-[:HAS_TOPIC]->(c);
"""


create_relation_edition_year = """
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
MATCH (y:Year { year: row.year })
MATCH (e:Edition { conference_edition: row.conference_edition })
CREATE (y)-[:OCURRED_DURING]->(e);
"""


