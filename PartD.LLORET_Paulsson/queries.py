

node_similarity = """
MATCH (n1:Paper {id: '729801'}), (n2:Paper {id: '735026'})
WITH n1, n2,
     [key IN keys(n1) WHERE key IN keys(n2) AND n1[key] = n2[key]] AS matching_properties,
     keys(n1) + [key IN keys(n2) WHERE NOT key IN keys(n1)] AS all_properties
RETURN n1.id AS node1_id, n2.id AS node2_id,
       matching_properties,
       toFloat(size(matching_properties)) / size(all_properties) AS similarity_score
       """

shortest_path_length = """
MATCH (start:Paper {id: '729351'}), (end:Paper {id: '729801'})
MATCH path = shortestPath((start)-[:CITES*]-(end))
RETURN path, length(path) AS pathLength
"""