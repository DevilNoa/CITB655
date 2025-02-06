import data_generation
import data_mart
import visualizations

# Генериране на данни
data_generation.generate_data()

# Зареждане на данни
products, users, orders = data_generation.load_data()

# Създаване на Data Mart
sales_data, total_sales_per_product, total_sales_per_user_type, daily_sales = data_mart.create_data_mart(products, users, orders)

# Създаване на визуализации
visualizations.plot_floating_sales_over_time(sales_data)
visualizations.plot_total_sales_per_product(total_sales_per_product)
visualizations.plot_total_sales_per_user_type(total_sales_per_user_type)
visualizations.plot_daily_sales(daily_sales)
