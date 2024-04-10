match_top_3 ="""
MATCH (paper:Paper)<-[:CITES]-(citingPaper)
MATCH (paper)-[:PRESENTED_IN]->(edition:Edition)-[:HAS_EDITION]-(conference:Conference)
WITH conference, paper, COUNT(citingPaper) AS citationCount

WITH conference, paper.id AS paperID, citationCount
ORDER BY conference.name, citationCount DESC

WITH conference, paperID[0..3] AS TopCitedPapers, citationCount as citations
RETURN conference.name, TopCitedPapers, citations
ORDER BY conference.name, citations DESC

"""

find_community = """
MATCH (author:Author)-[:AUTHORED]->(paper:Paper)-[:PRESENTED_IN]->(edition:Edition)<-[:HAS_EDITION]-(conference:Conference)
WITH conference, author, COUNT(DISTINCT edition) AS editionsCount
WHERE editionsCount >= 4
RETURN conference.name AS ConferenceName, author.name, editionsCount
"""

