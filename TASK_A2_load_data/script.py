from neo4j import GraphDatabase
from queries import (
    load_authors,
    load_article,
    create_relation_authors_article,
    load_time,
    load_journals,
    load_cities,
    load_conference_name,
    load_conference_edition,
    create_conference_edition_relation,
    create_city_edition_relation,
    create_relation_paper_journal,
    create_relation_year_journal,
    create_citations_data,
    load_communities,
    create_relation_paper_community,
    create_relation_edition_year,
    create_index_author,
    create_index_paper
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

clean_slate = '''
MATCH (n)
DETACH DELETE n
'''

clean_indexes = "DROP INDEX authorNameIndex IF EXISTS"
run_query(clean_indexes)

clean_indexes = "DROP INDEX paperIdIndex IF EXISTS"
run_query(clean_indexes)

run_query(clean_slate)

run_query(load_authors)
run_query(load_article)

run_query(create_index_author)
run_query(create_index_paper)

run_query(create_relation_authors_article)
run_query(load_time)
run_query(load_journals)
run_query(load_cities)
run_query(load_conference_name)
run_query(load_conference_edition)
run_query(create_conference_edition_relation)
run_query(create_city_edition_relation)
run_query(create_relation_paper_journal)
run_query(create_relation_year_journal)
run_query(create_citations_data)
run_query(load_communities)
run_query(create_relation_paper_community)
run_query(create_relation_edition_year)
