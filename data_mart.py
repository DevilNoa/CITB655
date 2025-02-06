import csv
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

def create_data_mart(products, users, orders):
    sales_data = {}
    total_sales_per_product = {}
    total_sales_per_user_type = {"customer": 0, "company": 0}
    daily_sales = {}

    for order in orders:
        date = order["date"]
        product_name = next(p["name"] for p in products if p["product_id"] == order["product_id"])
        user_type = next(u["user_type"] for u in users if u["user_id"] == order["user_id"])

        if date not in sales_data:
            sales_data[date] = {}
        if product_name not in sales_data[date]:
            sales_data[date][product_name] = {"total_sales": 0}
        sales_data[date][product_name]["total_sales"] += int(order["quantity"])

        total_sales_per_product[product_name] = total_sales_per_product.get(product_name, 0) + int(order["quantity"])
        total_sales_per_user_type[user_type] += int(order["quantity"])
        daily_sales[date] = daily_sales.get(date, 0) + int(order["quantity"])

    with open("data/fact_sales.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "top_product", "bottom_product"])
        for date, products in sales_data.items():
            top_product = max(products, key=lambda p: products[p]["total_sales"])
            bottom_product = min(products, key=lambda p: products[p]["total_sales"])
            writer.writerow([date, top_product, bottom_product])

    return sales_data, total_sales_per_product, total_sales_per_user_type, daily_sales
