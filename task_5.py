import json
import os

LIBRARY_FILE = 'library.json'
AVAILABLE_BOOKS_FILE = 'available_books.txt'

def load_library():
    if not os.path.exists(LIBRARY_FILE):
        return []
    
    try:
        with open(LIBRARY_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Ошибка чтения файла. Создана пустая библиотека.")
        return []

def save_library(books):
    with open(LIBRARY_FILE, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
    print("Данные сохранены в файл.")

def view_all_books(books):
    print("\n=== ВСЕ КНИГИ В БИБЛИОТЕКЕ ===")
    if not books:
        print("Библиотека пуста.")
        return
    
    for book in books:
        status = "доступна" if book['available'] else "выдана"
        print(f"\nID: {book['id']}")
        print(f"  Название: {book['title']}")
        print(f"  Автор: {book['author']}")
        print(f"  Год: {book['year']}")
        print(f"  Статус: {status}")
    print(f"\nВсего книг: {len(books)}")

def search_books(books):
    print("\n=== ПОИСК КНИГ ===")
    query = input("Введите название или автора для поиска: ").strip().lower()
    
    if not query:
        print("Поисковой запрос пуст.")
        return
    
    found_books = []
    for book in books:
        if (query in book['title'].lower() or 
            query in book['author'].lower()):
            found_books.append(book)
    
    if found_books:
        print(f"\nНайдено книг: {len(found_books)}")
        for book in found_books:
            status = "доступна" if book['available'] else "выдана"
            print(f"\nID: {book['id']}")
            print(f"  Название: {book['title']}")
            print(f"  Автор: {book['author']}")
            print(f"  Год: {book['year']}")
            print(f"  Статус: {status}")
    else:
        print("Книги не найдены.")

def add_book(books):
    print("\n=== ДОБАВЛЕНИЕ НОВОЙ КНИГИ ===")
    
    new_id = 1
    if books:
        new_id = max(book['id'] for book in books) + 1
    
    title = input("Введите название книги: ").strip()
    if not title:
        print("Ошибка: название книги не может быть пустым.")
        return
    
    author = input("Введите автора книги: ").strip()
    if not author:
        print("Ошибка: автор книги не может быть пустым.")
        return
    
    try:
        year = int(input("Введите год издания: "))
    except ValueError:
        print("Ошибка: год должен быть числом.")
        return
    
    new_book = {
        'id': new_id,
        'title': title,
        'author': author,
        'year': year,
        'available': True
    }
    
    books.append(new_book)
    print(f"\nКнига '{title}' успешно добавлена с ID: {new_id}")
    save_library(books)

def change_availability(books):
    print("\n=== ИЗМЕНЕНИЕ СТАТУСА ДОСТУПНОСТИ ===")
    
    try:
        book_id = int(input("Введите ID книги: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return
    
    book = find_book_by_id(books, book_id)
    
    if not book:
        print(f"Книга с ID {book_id} не найдена.")
        return
    
    if book['available']:
        book['available'] = False
        print(f"Книга '{book['title']}' выдана.")
    else:
        book['available'] = True
        print(f"Книга '{book['title']}' возвращена в библиотеку.")
    
    save_library(books)

def delete_book(books):
    print("\n=== УДАЛЕНИЕ КНИГИ ===")
    
    try:
        book_id = int(input("Введите ID книги для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return
    
    book = find_book_by_id(books, book_id)
    
    if not book:
        print(f"Книга с ID {book_id} не найдена.")
        return
    
    confirm = input(f"Вы уверены, что хотите удалить книгу '{book['title']}'? (да/нет): ").lower()
    
    if confirm == 'да':
        books.remove(book)
        print(f"Книга '{book['title']}' успешно удалена.")
        save_library(books)
    else:
        print("Удаление отменено.")

def export_available_books(books):
    print("\n=== ЭКСПОРТ ДОСТУПНЫХ КНИГ ===")
    
    available_books = [book for book in books if book['available']]
    
    if not available_books:
        print("Нет доступных книг для экспорта.")
        return
    
    with open(AVAILABLE_BOOKS_FILE, 'w', encoding='utf-8') as file:
        file.write("=== ДОСТУПНЫЕ КНИГИ В БИБЛИОТЕКЕ ===\n\n")
        file.write(f"Всего доступно: {len(available_books)}\n\n")
        
        for book in available_books:
            file.write(f"ID: {book['id']}\n")
            file.write(f"  Название: {book['title']}\n")
            file.write(f"  Автор: {book['author']}\n")
            file.write(f"  Год: {book['year']}\n\n")
    
    print(f"Список доступных книг экспортирован в файл '{AVAILABLE_BOOKS_FILE}'")

def find_book_by_id(books, book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return None

def show_menu():
    print("\n" + "="*40)
    print("       СИСТЕМА УЧЕТА КНИГ")
    print("="*40)
    print("1. Просмотр всех книг")
    print("2. Поиск книги по автору/названию")
    print("3. Добавить новую книгу")
    print("4. Изменить статус (взята/возвращена)")
    print("5. Удалить книгу по ID")
    print("6. Экспорт доступных книг в файл")
    print("0. Выход")
    print("="*40)

def main():
    print("Добро пожаловать в систему учета библиотеки!")
    
    books = load_library()
    
    while True:
        show_menu()
        choice = input("Выберите действие (0-6): ").strip()
        
        if choice == '1':
            view_all_books(books)
        elif choice == '2':
            search_books(books)
        elif choice == '3':
            add_book(books)
        elif choice == '4':
            change_availability(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            export_available_books(books)
        elif choice == '0':
            print("\nСпасибо за работу с системой учета!")
            break
        else:
            print("\nОшибка: неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()