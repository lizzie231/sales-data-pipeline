import csv

file_path = "data/raw_sales_data.csv"

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["unit_price"] = float(row["unit_price"])
        row["total_price"] = row["quantity"] * row["unit_price"]
        print(row)
