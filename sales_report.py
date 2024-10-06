import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def generate_sample_data(num_records=1000):
    np.random.seed(42)  # За възпроизводимост

    dates = pd.date_range(start='2023-01-01', end='2023-12-31', periods=num_records)
    products = ['Product A', 'Product B', 'Product C', 'Product D']

    data = {
        'Date': dates,
        'Product': np.random.choice(products, num_records),
        'Quantity': np.random.randint(1, 50, num_records),
        'Price': np.random.uniform(10, 100, num_records).round(2)
    }

    df = pd.DataFrame(data)
    df['Total'] = df['Quantity'] * df['Price']

    return df


# Генериране на данни
sales_data = generate_sample_data()
print(sales_data.head())


def basic_sales_analysis(df):
    # Обща сума на продажбите
    total_sales = df['Total'].sum()

    # Продажби по продукт
    product_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)

    # Средна цена на продукт
    avg_price = df.groupby('Product')['Price'].mean()

    # Брой продажби по месец
    monthly_sales = df.set_index('Date').resample('M')['Total'].sum()

    return total_sales, product_sales, avg_price, monthly_sales


# Извършване на анализа
total_sales, product_sales, avg_price, monthly_sales = basic_sales_analysis(sales_data)

print(f"Общи продажби: ${total_sales:.2f}")
print("\nПродажби по продукт:")
print(product_sales)
print("\nСредна цена на продукт:")
print(avg_price)
print("\nМесечни продажби:")
print(monthly_sales)