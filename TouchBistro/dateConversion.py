import csv
from datetime import datetime

def convert_to_iso(date_str):
    return datetime.strptime(date_str, "%a, %b %d, %Y").strftime("%Y-%m-%d")

def process_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            row[0] = convert_to_iso(row[0])
            writer.writerow(row)

input_filename = "nba_games.csv"
output_filename = "nba_games_cleansed.csv" 
process_csv(input_filename, output_filename)

print(f"Conversion completed. Check '{output_filename}'.")
