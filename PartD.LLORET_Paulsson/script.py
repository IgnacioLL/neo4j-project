
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from queries import node_similarity, shortest_path_length
from neo4j_connection import run_query



def main():
    results = run_query(node_similarity)
    # Print the results
    for result in results:
        print(f"Node 1 ID: {result['node1_id']}")
        print(f"Node 2 ID: {result['node2_id']}")
        print(f"Matching properties: {result['matching_properties']}")
        print(f"Similarity score: {result['similarity_score']:.4f}")


        
    results = run_query(shortest_path_length)
    # Print the results
    if results:
        for result in results:
            path = result['path']
            path_length = result['pathLength']
            
            print(f"Shortest path length: {path_length}")
            print("Path:")
            for i, item in enumerate(path):
                if i % 2 == 0:  # It's a node
                    node = item
                    print(f"  - Paper ID: {node['id']}, Title: {node['title']}")
                else:  # It's a relationship
                    rel = item
                    print(f"    {rel}")  # This will print the relationship type, e.g., 'CITES'
    else:
        print("No path found between the two papers.")


if __name__ == '__main__':
    main()