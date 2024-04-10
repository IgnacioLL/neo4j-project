import csv

def extract_first_10000_rows(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_input:
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_output:
            reader = csv.reader(csv_input)
            writer = csv.writer(csv_output)

            # Write header if present
            header = next(reader)
            writer.writerow(header)

            # Write first 10000 rows
            for i, row in enumerate(reader):
                if i >= 10000:
                    break
                writer.writerow(row)

if __name__ == "__main__":
    
    
    extract_first_10000_rows("edition_data.csv", "_edition_data.csv")
    
