from neo4j import GraphDatabase

# Define the connection URI and credentials
uri = "bolt://localhost:7687/"  # Your Neo4j URI
username = "neo4j"  # Your Neo4j username
password = "12345678"  # Your Neo4j password

# Define a function to run a Cypher query
def run_query(query):
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            result = session.run(query)
            records = result.data()
            return records

add_article = '''
LOAD CSV WITH HEADERS FROM 'file:///cleaned_article_data_small.csv' AS row
MERGE (:Paper { 
    year: row.year,
    id: row.id,
    title: CASE WHEN row.title IS NOT NULL THEN row.title ELSE '' END,
    url: row.url,
    volume: row.volume
});
'''


add_authors = '''
LOAD CSV WITH HEADERS FROM 'file:///cleaned_authors_data_limit.csv' AS row
MERGE (:Author { name: row.name, cleaned_name: row.cleaned_name, email: row.email });

'''

link_article_author = '''
LOAD CSV WITH HEADERS FROM 'file:///cleaned_article_data_small.csv' AS row
MERGE (a:Author { name: row.author_name })
MERGE (p:Paper { id: row.id })
MERGE (a)-[:AUTHORED]->(p);
'''


clean_slate = '''
MATCH (n)
DETACH DELETE n

'''

presented_in_edge = '''
LOAD CSV WITH HEADERS FROM 'file:///cleaned_article_data_small.csv' AS row
MATCH (p:Paper { id: row.id })
MATCH (e:Edition { name: row.edition })
MERGE (p)-[:PRESENTED_IN]->(e);

'''


chat_gpt_wrong_name = '''
LOAD CSV WITH HEADERS FROM 'file:///article.csv' AS row
CREATE (:Paper { 
    year: row.year,
    id: row.id,
    title: row.title,
    url: row.url,
    volume: row.volume
});

// Import Conferences
LOAD CSV WITH HEADERS FROM 'file:///conference_data.csv' AS row
CREATE (:Conference { name: row.conference_name });

// Import Conference Editions
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
MATCH (c:Conference { name: row.conference_name })
CREATE (:Edition { name: row.conference_edition, city: row.city })
CREATE (c)-[:HAS_EDITION]->(e);

// Import Journals
LOAD CSV WITH HEADERS FROM 'file:///journal.csv' AS row
CREATE (:Journal { name: row.journal, rank: row.rank });

// Import Reviewers
LOAD CSV WITH HEADERS FROM 'file:///reviewer.csv' AS row
CREATE (:Reviewer { ID: row.ID, reviewer: row.reviewer });

// Import Reviewer Data
LOAD CSV WITH HEADERS FROM 'file:///reviewer_data.csv' AS row
MATCH (r:Reviewer { ID: row.reviewer })
MATCH (e:Edition { name: row.edition })
CREATE (r)-[:ASSIGNED_TO]->(e);

// Import City Data
LOAD CSV WITH HEADERS FROM 'file:///city_data.csv' AS row
CREATE (:City { name: row.city });
'''




# Execute the query
run_query(cypher_query_data)

result = run_query(cypher_query)

