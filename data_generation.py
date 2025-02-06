import csv
import random
import os
from datetime import datetime, timedelta

categories = [
    "Laptop", "Smartphone", "Tablet", "TV", "Gaming Consoles", "Smartwatches", "Cameras", "Speakers",
    "Gaming Peripherals", "Biometric Devices", "PC Components"
]

real_product_names = [
    "MacBook Pro", "iPhone 14", "Samsung Galaxy Tab", "LG OLED TV", "PlayStation 5",
    "Apple Watch", "Canon DSLR Camera", "JBL Bluetooth Speaker", "Logitech Gaming Mouse",
    "Fingerprint Scanner", "AMD Ryzen 9 CPU", "Dell XPS Laptop", "Sony Bravia TV",
    "Xbox Series X", "Garmin Smartwatch", "Nikon Mirrorless Camera", "Bose Sound System",
    "Razer Keyboard", "VR Headset", "Intel i9 Processor"
]

def generate_data():
    os.makedirs("data", exist_ok=True)

    products = [
        {"product_id": i, "name": real_product_names[i - 1], "upc_code": f"UPC{i:05d}", "category": random.choice(categories),
         "price": random.randint(500, 2000), "stock": random.randint(10, 50)}
        for i in range(1, 21)
    ]

    with open("data/products.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)

    users = [
        {"user_id": i, "user_type": random.choice(["customer", "company"]), "name": f"User {i}"}
        for i in range(1, 11)
    ]

    with open("data/users.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)

    orders = [
        {"order_id": i, "user_id": random.randint(1, 10), "product_id": random.randint(1, 20),
         "quantity": random.randint(1, 3), "total_price": 0,
         "date": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")}
        for i in range(1, 6001)
    ]

    for order in orders:
        product = next((p for p in products if p["product_id"] == order["product_id"]), None)
        if product:
            order["total_price"] = product["price"] * order["quantity"]

    with open("data/orders.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=orders[0].keys())
        writer.writeheader()
        writer.writerows(orders)

def load_data():
    with open("data/products.csv", "r") as f:
        products = list(csv.DictReader(f))

    with open("data/users.csv", "r") as f:
        users = list(csv.DictReader(f))

    with open("data/orders.csv", "r") as f:
        orders = list(csv.DictReader(f))

    return products, users, orders
