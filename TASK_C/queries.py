find_relevant_authors_journal_community_database ="""
MATCH (co:Communities)<-[:TOPIC]-(p:Paper)-[:PUBLISHED_IN]->(j:Journal)
WITH j, COUNT(DISTINCT p) AS papersCount
MATCH (co:Communities)<-[:TOPIC]-(p:Paper)-[:PUBLISHED_IN]->(j:Journal)
where co.category = 'database'
WITH j, COUNT(p) as conteo, papersCount
WITH j, (conteo*1.0 / papersCount) as prc
where prc > .9
MATCH (jo:Journal)<-[:PUBLISHED_IN]-(p:Paper)<-[:CITES]-(citingPaper) 
MATCH (co:Communities)<-[:TOPIC]-(p:Paper)
where jo.name = j.name AND co.category = 'database'
WITH j.name as journal_name, p, COUNT(citingPaper) AS citationCount
ORDER BY journal_name, citationCount DESC

// Collect the top 10 papers for each journal
WITH journal_name, citationCount, COLLECT(p)[0..10] AS topPapers

// Unwind the top papers to match authors
UNWIND topPapers AS topPaper
MATCH (a:Author)-[:AUTHORED]->(topPaper)
WITH journal_name, topPaper.title AS paper_title, topPaper.id AS paper_id, citationCount, COLLECT(a.name) AS author_names

// Collect the results for each journal
RETURN journal_name, citationCount, COLLECT({paper_id: paper_id, paper_title: paper_title, authors: author_names}) AS top_cited_papers
"""

create_relation_paper_community = """
MATCH (p:Paper), (co:Communities)
WHERE p.id = co.article_id
CREATE (p)-[:TOPIC]->(co);
"""