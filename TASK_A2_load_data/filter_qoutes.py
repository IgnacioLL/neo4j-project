import csv

input_file = 'article_data_limit.csv'
output_file = 'cleaned_article_data_limit.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if all('"' not in field for field in row):
            
            writer.writerow(row)
        else:
            print("hej")