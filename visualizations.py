import matplotlib.pyplot as plt


def create_visualizations(product_sales, monthly_sales):
    plt.style.use('seaborn')

    # Графика на продажбите по продукт
    plt.figure(figsize=(10, 6))
    product_sales.plot(kind='bar')
    plt.title('Общи продажби по продукт')
    plt.xlabel('Продукт')
    plt.ylabel('Обща сума продажби')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('product_sales.png')
    plt.close()

    # Графика на месечните продажби
    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Месечни продажби')
    plt.xlabel('Месец')
    plt.ylabel('Обща сума продажби')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('monthly_sales.png')
    plt.close()

    # Кръгова диаграма за дял на продажбите по продукт
    plt.figure(figsize=(8, 8))
    plt.pie(product_sales, labels=product_sales.index, autopct='%1.1f%%', startangle=90)
    plt.title('Дял на продажбите по продукт')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('sales_distribution.png')
    plt.close()

    print("Визуализациите са създадени и запазени като PNG файлове.")