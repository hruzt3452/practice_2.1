def create_file(filename="text.txt"):
    try:
        with open(filename, "w", encoding='utf-8') as file:
            file.write("Хаай\n")
            file.write("Ватс ё нэйм\n")
            file.write("зис ис май фёрст файл\n")
            file.write("ай эм э програмисст\n")
            file.write("зэ энд\n")
    except IOError:
        print("Ошибка!! Не получилось создать файл.")

def count_lines(lines_list):
    count = len(lines_list)
    print("1. Количество строк в файле:", count)

def count_words(lines_list):
    full_text = "".join(lines_list)
    words = full_text.split()
    print("2. Количество слов в файле:", len(words))

def find_longest_line(lines_list):
    if not lines_list:
        print("Файл пуст.")
        return
    
    longest = max(lines_list, key=lambda s: len(s.strip()))
    print("3. Самая длинная строка:", longest.strip())

def main():
    filename = "text.txt"
    create_file(filename)
    
    try:
        with open(filename, "r", encoding='utf-8') as file:
            lines = file.readlines()
        
        count_lines(lines)
        count_words(lines)
        find_longest_line(lines)
        
    except FileNotFoundError:
        print("Ошибка!! Файл не найден.")
    except IOError:
        print("Ошибка!! Проблема с чтением файла.")

if __name__ == '__main__':
    main()