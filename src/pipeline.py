import csv

file_path = "data/raw_sales_data.csv"

with open(file_path, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
