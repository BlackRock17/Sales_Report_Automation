from datetime import datetime


def generate_html_report(total_sales, product_sales, avg_price, monthly_sales):
    html_content = f"""
    <html>
    <head>
        <title>Отчет за продажбите</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }}
            h1 {{ color: #333366; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Отчет за продажбите</h1>
        <p>Дата на генериране: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

        <h2>Обобщение на продажбите</h2>
        <p>Общи продажби: ${total_sales:.2f}</p>

        <h2>Продажби по продукт</h2>
        <table>
            <tr><th>Продукт</th><th>Обща сума продажби</th></tr>
            {''.join(f"<tr><td>{product}</td><td>${sales:.2f}</td></tr>" for product, sales in product_sales.items())}
        </table>

        <h2>Средна цена на продукт</h2>
        <table>
            <tr><th>Продукт</th><th>Средна цена</th></tr>
            {''.join(f"<tr><td>{product}</td><td>${price:.2f}</td></tr>" for product, price in avg_price.items())}
        </table>

        <h2>Визуализации</h2>
        <img src="product_sales.png" alt="Продажби по продукт">
        <img src="monthly_sales.png" alt="Месечни продажби">
        <img src="sales_distribution.png" alt="Разпределение на продажбите">

    </body>
    </html>
    """

    with open('sales_report.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("HTML отчетът е генериран и запазен като 'sales_report.html'")