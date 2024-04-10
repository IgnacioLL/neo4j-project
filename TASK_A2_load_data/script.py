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

clean_slate = '''
MATCH (n)
DETACH DELETE n

'''


query_list = '''
LOAD CSV WITH HEADERS FROM 'file:///_authors_data_limit.csv' AS row
MERGE (a:Author { 
    name: row.name,
    cleaned_name: row.cleaned_name,
    email: row.email
});

// Import Papers
LOAD CSV WITH HEADERS FROM 'file:///_article_data_limit.csv' AS row
MERGE (p:Paper { 
    year: row.year,
    id: row.id,
    title: COALESCE(row.title, ''),
    url: row.url,
    volume: row.volume
})
WITH p, row
MATCH (a:Author { name: row.author_name })
MERGE (a)-[:AUTHORED]->(p);

// import time
LOAD CSV WITH HEADERS FROM 'file:///time.csv' AS row
MERGE (y:Year { value: toInteger(row.year) });

// Import Journals
LOAD CSV WITH HEADERS FROM 'file:///journal_data_w_rank.csv' AS row
MERGE (j:Journal { id: row.journal })
SET j.name = row.journal,
    j.rank = row.rank;

// Import Cities
LOAD CSV WITH HEADERS FROM 'file:///city_data.csv' AS row
MERGE (ct:City { name: row.city });

// Import Conferences
LOAD CSV WITH HEADERS FROM 'file:///conference_data.csv' AS row
WITH row WHERE row.conference_name IS NOT NULL
MERGE (c:Conference { conference_name: row.conference_name })
SET c.name = COALESCE(row.conference_name, '')


// Import Conference Editions
LOAD CSV WITH HEADERS FROM 'file:///_edition_data.csv' AS row
MERGE (e:Edition { name: row.conference_edition })
SET e.city = row.city;

// Edge between Conf and Edition
LOAD CSV WITH HEADERS FROM 'file:///_edition_data.csv' AS row
MATCH (c:Conference { name: row.conference_name })
MATCH (e:Edition { name: row.conference_edition, city: row.city })
CREATE (c)-[:HAS_EDITION]->(e);





'''




# Execute the query
run_query(cypher_query_data)

result = run_query(cypher_query)

