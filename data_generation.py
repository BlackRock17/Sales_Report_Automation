import pandas as pd
import numpy as np


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
