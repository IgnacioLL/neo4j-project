import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import BASE_URL

match_top_3 =f"""
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


impact_factor = """
MATCH (j:Journal)<-[:PUBLISHED_IN]-(a:Paper)
WHERE a.year IN [toString(toInteger(date().year) - 2), toString(toInteger(date().year) - 1)]
WITH j, count(a) AS articles_count
MATCH (j)<-[:PUBLISHED_IN]-(a:Paper)<-[:CITES]-(c:Paper)
WHERE a.year IN [toString(toInteger(date().year) - 2), toString(toInteger(date().year) - 1)]
WITH j, articles_count, count(c) AS citations_count
WHERE articles_count > 0
RETURN j.name AS journal, toFloat(citations_count) / articles_count AS impact_factor
ORDER BY impact_factor DESC
LIMIT 10
"""

h_index = """
MATCH (a:Author)-[:AUTHORED]->(p:Paper)<-[:CITES]-(c:Paper)
WITH a, p, count(c) AS citations
ORDER BY a, citations DESC
WITH a, collect(citations) AS citation_counts
WITH a, [c IN citation_counts WHERE c >= size(range(1, c))] AS h_candidates
RETURN a.name AS author, CASE WHEN size(h_candidates) > 0 THEN size(h_candidates) ELSE 0 END AS h_index
ORDER BY h_index ASC
LIMIT 10
"""