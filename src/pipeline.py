import csv
from datetime import datetime

file_path = "data/raw_sales_data.csv"

cleaned_data = []

# Read the raw sales data from the CSV file
with open(file_path, "r") as file:
    reader = csv.DictReader(file)

# Clean and transform the data
    for row in reader:
        # Validate and parse the order_date field
        try:
            parsed_date = datetime.strptime(
                row["order_date"], "%Y-%m-%d").date()
            row["parsed_order_date"] = parsed_date
            row["order_date_valid"] = True
        except ValueError:
            row["parsed_order_date"] = None
            row["order_date_valid"] = False
        row["parsed_order_date"] = parsed_date
        row["quantity"] = int(row["quantity"])
        row["unit_price"] = float(row["unit_price"])
        row["total_price"] = row["quantity"] * row["unit_price"]
        cleaned_data.append(row)

# Write the cleaned data to a new CSV file
output_file = "data/cleaned_sales_data.csv"

fieldnames = [
    "order_id",
    "order_date",
    "parsed_order_date",
    "order_date_valid",
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
