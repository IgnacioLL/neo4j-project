import sys 
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from neo4j_connection import run_query

from queries import (
    load_communities,
    create_relation_paper_community,
    find_relevant_authors_journal_community_database

)

def main():
    results = run_query(load_communities) ## Load communities
    
    ## Create relation paper community
    results = run_query(create_relation_paper_community)

    ## Find relevant authors
    results = run_query(find_relevant_authors_journal_community_database)
    for result in results[:10]:
        print(result)


if __name__ == '__main__':
    main()