with open('students.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

good_students = []
best_student_name = ""
best_student_avg = 0     # средний балл

for line in lines:
    line = line.strip()
    if not line:
        continue
    parts = line.split(':')
    name = parts[0]
    grades_str = parts[1]
    grades = [int(g) for g in grades_str.split(',')]
    average = sum(grades) / len(grades)

    if average > 4.0:
        good_students.append(f"{name}:{average:.2f}\n")

    if average > best_student_avg:
        best_student_avg = average
        best_student_name = name

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for student in good_students:
        result_file.write(student)

print(f"Студент с наивысшим средним баллом: {best_student_name}")
print(f"Его средний балл: {best_student_avg:.2f}")