import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from queries import (
    load_authors,
    load_article,
    create_relation_authors_article,
    load_time,
    load_journals,
    load_city,
    load_conference,
    load_edition,
    create_relation_paper_journal,
    create_relation_year_journal,
    create_citations_data,
    create_relation_paper_edition,
    create_index_author,
    create_index_paper
)


from neo4j_connection import run_query

def clean():
    clean_slate = '''
    MATCH (n)
    DETACH DELETE n
    '''

    clean_indexes = "DROP INDEX authorNameIndex IF EXISTS"
    run_query(clean_indexes)

    clean_indexes = "DROP INDEX paperIdIndex IF EXISTS"
    run_query(clean_indexes)
    run_query(clean_slate)



def main():

    print("Deleting previous information:...")
    clean()
    
    print("End deleting information:...")
    print("Loading data...")

    run_query(load_authors)
    print("Loaded authors data")

    run_query(load_article)
    print("Loaded articles data")

    run_query(create_index_author)
    run_query(create_index_paper)
    print("Index created")

    run_query(load_time)
    print("Loaded time data")

    run_query(load_journals)
    print("Loaded Journal data")

    run_query(load_city)
    print("Loaded city")

    run_query(load_edition)
    print("Loaded edition")

    run_query(load_conference)
    print("Loaded conference")

    run_query(create_relation_year_journal)
    print("Journal relation created")

    run_query(create_citations_data)
    print("Citations relation created")
    
    run_query(create_relation_paper_journal)
    print("Journal relation created")

    run_query(create_relation_authors_article)
    print("Authors article relation created")

    run_query(create_relation_paper_edition)
    print("Edition paper relation created")

    print("End")

if __name__ == '__main__':
    main()