import sys 
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from neo4j_connection import run_query
from queries import (
    match_top_3,
    find_community,
    impact_factor,
    h_index
)
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import from neo4j_connection
from neo4j_connection import run_query

def main():

    ## Match top3
    print("Match top 3: \n")
    results = run_query(match_top_3)
    for result in results[:10]:
        print(result)
    print("##########################################################################################################\n")

    ## Find community
    print("Find community: \n")
    results = run_query(find_community) ## Unluckily empty
    print(results)
    print("##########################################################################################################\n")


    ## Impactor factor
    print("Impact factor: \n")
    results = run_query(impact_factor)
    for result in results:
        print(result)
    print("##########################################################################################################\n")
    

    print("H-Index: \n")
    ## H-INDEX
    results = run_query(h_index) ## No interesting at all, everything 1 because each author has only 1 paper in the data
    for result in results:
        print(result)
    print("##########################################################################################################\n")

if __name__ == '__main__':
    main()
