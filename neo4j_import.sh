#!/bin/bash
bin/neo4j-admin database import full \
    dblp.db \
    --overwrite-destination \
    --delimiter ";" \
    --array-delimiter "|" \
    --id-type INTEGER \
    --nodes=mastersthesis="../data/dblp_mastersthesis_header.csv,../data/dblp_mastersthesis.csv" \
    --nodes=incollection="../data/dblp_incollection_header.csv,../data/dblp_incollection.csv" \
    --nodes=proceedings="../data/dblp_proceedings_header.csv,../data/dblp_proceedings.csv" \
    --nodes=article="../data/dblp_article_header.csv,../data/dblp_article.csv" \
    --nodes=data="../data/dblp_data_header.csv,../data/dblp_data.csv" \
    --nodes=inproceedings="../data/dblp_inproceedings_header.csv,../data/dblp_inproceedings.csv" \
    --nodes=book="../data/dblp_book_header.csv,../data/dblp_book.csv" \
    --nodes=www="../data/dblp_www_header.csv,../data/dblp_www.csv" \
    --nodes=phdthesis="../data/dblp_phdthesis_header.csv,../data/dblp_phdthesis.csv" \
    --nodes=journal="../data/dblp_journal.csv" \
    --relationships=published_in="../data/dblp_journal_published_in.csv" \
    --nodes=author="../data/dblp_author.csv" \
    --relationships=authored_by="../data/dblp_author_authored_by.csv"
