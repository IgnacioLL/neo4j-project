from neo4j import GraphDatabase
from queries import (
    load_communities,
    create_relation_paper_community

)

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
        

run_query(load_communities)
run_query(create_relation_paper_community)
