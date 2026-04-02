import csv

FILENAME = 'products.csv'
FIELDNAMES = ['Название', 'Количество', 'Цена']

def read_products(filename):
    products = []
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Количество'] = int(row['Количество'])
                row['Цена'] = int(row['Цена'])
                products.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создадим новый при сохранении.")
    return products

def write_products(filename, products):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(products)
    print(f"Данные успешно сохранены в {filename}")

def add_product(products):
    print("\n--- Добавление товара ---")
    name = input("Введите название товара: ").strip()
    
    if not name:
        print("Ошибка: Название не может быть пустым!")
        return

    try:
        quantity = int(input("Введите количество: "))
        price = int(input("Введите цену: "))
        
        new_product = {
            'Название': name,
            'Количество': quantity,
            'Цена': price
        }
        products.append(new_product)
        print(f"Товар '{name}' добавлен!")
        
    except ValueError:
        print("Ошибка: Количество и цена должны быть числами!")

def search_product(products):
    print("\n--- Поиск товара ---")
    search_name = input("Введите название для поиска: ").strip().lower()
    
    if not search_name:
        print("Ошибка: Введите название для поиска!")
        return

    found = False
    for product in products:
        if search_name in product['Название'].lower():
            print(f"Найдено: {product['Название']} | Кол-во: {product['Количество']} | Цена: {product['Цена']}")
            found = True
    
    if not found:
        print("Товары с таким названием не найдены.")

def calculate_total_value(products):
    print("\n--- Общая стоимость склада ---")
    total = 0
    for product in products:
        item_total = product['Цена'] * product['Количество']
        total += item_total
    
    print(f"Общая стоимость всех товаров: {total} руб.")
    return total

def show_all_products(products):
    print("\n--- Все товары на складе ---")
    if not products:
        print("Склад пуст.")
        return
    
    print(f"{'Название':<15} | {'Количество':<10} | {'Цена':<10}")
    print("-" * 45)
    for product in products:
        print(f"{product['Название']:<15} | {product['Количество']:<10} | {product['Цена']:<10}")

def main():
    print("Добро пожаловать в систему управления складом!")
    
    products = read_products(FILENAME)
    
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Показать все товары")
        print("2. Добавить товар")
        print("3. Поиск товара")
        print("4. Расчет общей стоимости")
        print("5. Сохранить и выйти")
        
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == '1':
            show_all_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            search_product(products)
        elif choice == '4':
            calculate_total_value(products)
        elif choice == '5':
            write_products(FILENAME, products)
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()