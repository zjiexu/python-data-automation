import csv

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output_clean.csv"

def clean_row(row):
    '''
    Remove leading and trailing whitespace from all string values in a row.
    '''
    return {
        key: value.strip() if isinstance(value, str) else value for key, value in row.items()
    }

with open(INPUT_FILE, newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    rows = [clean_row(row) for row in reader]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Data cleaning completed. Output saved to output_clean.csv")