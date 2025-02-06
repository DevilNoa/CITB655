import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("visualizations", exist_ok=True)

def plot_floating_sales_over_time(sales_data):
    dates = sorted(sales_data.keys())
    plt.figure(figsize=(12, 6))
    for product in set(p for d in sales_data.values() for p in d.keys()):
        sales = np.cumsum([sales_data[date].get(product, {"total_sales": 0})["total_sales"] for date in dates])
        plt.plot(dates, sales, marker="o", linestyle="-", label=product)
    plt.xlabel("Date")
    plt.ylabel("Cumulative Sales Count")
    plt.title("Cumulative Sales Over Time (Per Product)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig("visualizations/daily_sales.png")
    plt.close()

def plot_total_sales_per_product(total_sales_per_product):
    plt.figure(figsize=(12, 6))
    products, sales = zip(*total_sales_per_product.items())
    plt.bar(products, sales, color='skyblue')
    plt.xlabel("Product Name")
    plt.ylabel("Total Sales")
    plt.title("Total Sales Per Product")
    plt.xticks(rotation=45)
    plt.savefig("visualizations/total_sales_per_product.png")
    plt.close()

def plot_total_sales_per_user_type(total_sales_per_user_type):
    plt.figure(figsize=(6, 6))
    labels, sales = zip(*total_sales_per_user_type.items())
    plt.pie(sales, labels=labels, autopct='%1.1f%%', colors=["blue", "orange"], startangle=140)
    plt.title("Total Sales by User Type")
    plt.savefig("visualizations/total_sales_per_user_type.png")
    plt.close()

def plot_daily_sales(daily_sales):
    dates, sales = zip(*sorted(daily_sales.items()))
    plt.figure(figsize=(12, 6))
    plt.plot(dates, sales, marker="o", linestyle="-", color='blue')
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.title("Total Sales Per Day")
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig("visualizations/daily_sales_per_day.png")
    plt.close()
