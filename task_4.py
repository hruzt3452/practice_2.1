import datetime  
import os

LOG_FILE = 'calculator.log'

def get_last_logs(filename, count=5):
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines[-count:]
    except Exception:
        return []

def log_operation(filename, num1, op, num2, result):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    
    log_entry = f"{timestamp} {num1} {op} {num2} = {result}\n"
    
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(log_entry)

def clear_log(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        pass
    print("Лог-файл успешно очищен.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль невозможно!")
            return None
        return num1 / num2
    else:
        print("Ошибка: неизвестная операция!")
        return None

def main():
    print("=== Калькулятор с логированием ===")
    
    print("\n--- История (последние 5 операций) ---")
    history = get_last_logs(LOG_FILE)
    if history:
        for line in history:
            print(line.strip())
    else:
        print("История пуста.")
    
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Выполнить вычисление")
        print("2. Очистить лог-файл")
        print("3. Выход")
        
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == '1':
            n1 = get_number("Введите первое число: ")
            n2 = get_number("Введите второе число: ")
            operation = input("Введите операцию (+, -, *, /): ").strip()
            
            result = calculate(n1, n2, operation)
            
            if result is not None:
                print(f"Результат: {result}")
                log_operation(LOG_FILE, n1, operation, n2, result)
                
        elif choice == '2':
            confirm = input("Вы уверены? История будет удалена (да/нет): ").lower()
            if confirm == 'да':
                clear_log(LOG_FILE)
            else:
                print("Отмена.")
                
        elif choice == '3':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()