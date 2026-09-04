import csv

file_path = "data/raw_sales_data.csv"

cleaned_data = []

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["unit_price"] = float(row["unit_price"])
        row["total_price"] = row["quantity"] * row["unit_price"]
        cleaned_data.append(row)

output_file = "data/cleaned_sales_data.csv"

fieldnames = [
    "order_id",
    "order_date",
    "customer_id",
    "customer_name",
    "product",
    "category",
    "quantity",
    "unit_price",
    "state",
    "total_price"
]

with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_data)
