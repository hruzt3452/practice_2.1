def read_students(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def parse_line(line):
    line = line.strip()
    if not line:
        return None, None
    
    parts = line.split(':')
    name = parts[0]
    grades = [int(g) for g in parts[1].split(',')]
    return name, grades

def calculate_average(grades):
    return sum(grades) / len(grades)

def write_result(filename, students_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for student in students_list:
            file.write(student + '\n')

def main():
    input_file = 'students.txt'
    output_file = 'result.txt'
    threshold = 4.0

    lines = read_students(input_file)

    good_students = []
    best_student_name = ""
    best_student_avg = 0

    for line in lines:
        name, grades = parse_line(line)
        
        if name is None:
            continue

        avg = calculate_average(grades)

        if avg > threshold:
            good_students.append(f"{name}:{avg:.2f}")

        if avg > best_student_avg:
            best_student_avg = avg
            best_student_name = name

    write_result(output_file, good_students)

    print(f"Студент с наивысшим средним баллом: {best_student_name}")
    print(f"Его средний балл: {best_student_avg:.2f}")
    print(f"\nРезультат записан в {output_file}")

if __name__ == "__main__":
    main()