import pandas as pd


def basic_sales_analysis(df):
    total_sales = df['Total'].sum()
    product_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)
    avg_price = df.groupby('Product')['Price'].mean()
    monthly_sales = df.set_index('Date').resample('ME')['Total'].sum()

    return total_sales, product_sales, avg_price, monthly_sales