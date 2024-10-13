import csv

# Read the CSV file and generate markdown table
with open('_data/companies.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    # Print header
    print(f"| {' | '.join(header)} |")
    print("|" + " | ".join(['---'] * len(header)) + "|")

    # Print each row
    for row in csv_reader:
        print(f"| {' | '.join(row)} |")
