import csv
import os

CSV_PATH = os.path.join("resources", "budget_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Open the CSV using the UTF-8 encoding
with open(CSV_PATH, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    monthcount = 0

    for row in csvreader:
        monthcount += 1

print(monthcount)
print(f'Total Months: {monthcount}')