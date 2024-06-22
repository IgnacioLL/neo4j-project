import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from queries import (
    create_relation_rewiews,
    set_approved,
    create_relation_affiliation
)
from neo4j_connection import run_query
        
def main():
    ## Create relation of reviews
    results = run_query(create_relation_rewiews) ## No results

    ## Add attribute approved
    results = run_query(set_approved) ## No results
    
    ## Create relation affiliation
    results = run_query(create_relation_affiliation) ## No results

if __name__ == '__main__':
    main()
