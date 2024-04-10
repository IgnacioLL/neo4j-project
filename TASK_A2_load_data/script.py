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
MERGE (y:Year { value: row.year });

// Import Journals
LOAD CSV WITH HEADERS FROM 'file:///_article_data_limit.csv' AS row
WITH DISTINCT row.journal AS journal
MERGE (j:Journal { name: journal });
    

// Import Cities
LOAD CSV WITH HEADERS FROM 'file:///city_data.csv' AS row
MERGE (ct:City { name: row.city });

// Import Conferences
LOAD CSV WITH HEADERS FROM 'file:///conference_data.csv' AS row
WITH row WHERE row.conference_name IS NOT NULL
MERGE (c:Conference { conference_name: row.conference_name })
SET c.name = COALESCE(row.conference_name, '');

// NEED QUERY SPLIT HERE

// Import Conference Editions
LOAD CSV WITH HEADERS FROM 'file:///_edition_data.csv' AS row
MERGE (e:Edition { name: row.conference_edition })
SET e.city = row.city;

// Create Relationships between Conf and Edition
LOAD CSV WITH HEADERS FROM 'file:///_edition_data.csv' AS row
MATCH (c:Conference { name: row.conference_name })
MATCH (e:Edition { name: row.conference_edition, city: row.city })
CREATE (c)-[:HAS_EDITION]->(e);

// Create Relationships between Conferences and Cities
LOAD CSV WITH HEADERS FROM 'file:///edition_data.csv' AS row
MATCH (c:Conference { name: row.conference_name })
MATCH (ct:City { name: row.city })
MERGE (c)-[:HELD_IN]->(ct);

// Create relationship between Paper and Journal
LOAD CSV WITH HEADERS FROM 'file:///_article_data_limit.csv' AS row
MATCH (p:Paper { id: row.id })
MATCH (j:Journal)
WHERE j.name = row.journal
MERGE (p)-[:PUBLISHED_IN]->(j);

// Create relationship between year and journal
LOAD CSV WITH HEADERS FROM 'file:///your_file.csv' AS row
MATCH (j:Journal { name: row.journal })
MATCH (y:Year { value: row.year })
MERGE (j)-[:OCCURRED_DURING]->(y);



'''




# Execute the query
run_query(cypher_query_data)

result = run_query(cypher_query)

