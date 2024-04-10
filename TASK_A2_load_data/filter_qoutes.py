import csv

input_file = '../temporal_zone/data/article_data.csv'
output_file = '../temporal_zone/data/cleaned_article_data_limit.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if all('"' not in field for field in row):
            writer.writerow(row)
        else:
            print("hej")