from data_generation import generate_sample_data
from data_analysis import basic_sales_analysis
from visualizations import create_visualizations
from report_generation import generate_html_report


def generate_automated_sales_report():
    # Генериране на данни
    sales_data = generate_sample_data()

    # Анализ на данните
    total_sales, product_sales, avg_price, monthly_sales = basic_sales_analysis(sales_data)

    # Създаване на визуализации
    create_visualizations(product_sales, monthly_sales)

    # Генериране на HTML отчет
    generate_html_report(total_sales, product_sales, avg_price, monthly_sales)

    print("Автоматизираният отчет за продажбите е генериран успешно!")


if __name__ == "__main__":
    generate_automated_sales_report()