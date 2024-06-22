from neo4j import GraphDatabase
from config import NEO4J_PASSWORD, NEO4J_USERNAME, NEO4J_URI

# Define a function to run a Cypher query
def run_query(query):
    with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)) as driver:
        with driver.session() as session:
            result = session.run(query)
            records = result.data()
            return records