from neo4j import GraphDatabase

# Define the connection URI and credentials
uri = "bolt://localhost:7687/"  # Your Neo4j URI
username = "neo4j"  # Your Neo4j username
password = "sdm-project"  # Your Neo4j password

# Define a function to run a Cypher query
def run_query(query):
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            result = session.run(query)
            records = result.data()
            return records

clean_slate = '''
MATCH (n)
DETACH DELETE n
'''
run_query(clean_slate)



clean_indexes = "DROP INDEX authorNameIndex IF EXISTS"
run_query(clean_indexes)

clean_indexes = "DROP INDEX paperIdIndex IF EXISTS"
run_query(clean_indexes)



loading_authors = """
LOAD CSV WITH HEADERS FROM 'file:///authors_data.csv' AS row
CREATE (a:Author { 
    name: row.name,
    cleaned_name: row.cleaned_name,
    author_id: row.author_id,
    email: row.email
});
"""

run_query(loading_authors)

loading_articles = """

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

run_query(loading_articles)


create_index_paper= "CREATE INDEX authorNameIndex FOR (a:Author) ON (a.author_id);"
run_query(create_index_paper)

create_index_article = "CREATE INDEX paperIdIndex FOR (p:Paper) ON (p.id);"
run_query(create_index_article)

mathcing_authors_articles = """
LOAD CSV WITH HEADERS FROM 'file:///article_authors_relation.csv' AS row
MATCH (a:Author {author_id: row.author_id})
MATCH (p:Paper {id: row.article_id})
CREATE (a)-[:AUTHORED]->(p);
"""

run_query(mathcing_authors_articles)



# query_list = '''
# LOAD CSV WITH HEADERS FROM 'file:///authors_data.csv' AS row
# CREATE (a:Author { 
#     name: row.name,
#     cleaned_name: row.cleaned_name,
#     email: row.email
# });

# // Import Papers
# LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
# CREATE (p:Paper { 
#     year: row.year,
#     id: row.id,
#     title: COALESCE(row.title, ''),
#     url: row.url,
#     volume: row.volume
# })
# WITH p, row
# MATCH (a:Author { name: row.author_name })
# CREATE (a)-[:AUTHORED]->(p);

# // import time
# LOAD CSV WITH HEADERS FROM 'file:///time.csv' AS row
# CREATE (y:Year { value: row.year });

# // Import Journals
# LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
# WITH DISTINCT row.journal AS journal
# CREATE (j:Journal { name: journal });
    

# // Import Cities
# LOAD CSV WITH HEADERS FROM 'file:///city_data.csv' AS row
# CREATE (ct:City { name: row.city });

# // Import Conferences
# LOAD CSV WITH HEADERS FROM 'file:///conference_data.csv' AS row
# WITH row WHERE row.conference_name IS NOT NULL
# CREATE (c:Conference { conference_name: row.conference_name })
# SET c.name = COALESCE(row.conference_name, '');

# // NEED QUERY SPLIT HERE

# // Import Conference Editions
# LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
# CREATE (e:Edition { name: row.conference_edition })
# SET e.city = row.city;

# // Create Relationships between Conf and Edition
# LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
# MATCH (c:Conference { name: row.conference_name })
# MATCH (e:Edition { name: row.conference_edition, city: row.city })
# CREATE (c)-[:HAS_EDITION]->(e);

# // Create Relationships between Conferences and Cities
# LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
# MATCH (c:Conference { name: row.conference_name })
# MATCH (ct:City { name: row.city })
# CREATE (c)-[:HELD_IN]->(ct);

# // Create relationship between Paper and Journal
# LOAD CSV WITH HEADERS FROM 'file:///article_data.csv' AS row
# MATCH (p:Paper { id: row.id })
# MATCH (j:Journal)
# WHERE j.name = row.journal
# CREATE (p)-[:PUBLISHED_IN]->(j);

# '''




# # Execute the query
# run_query(query_list)

# result = run_query(query_list)

