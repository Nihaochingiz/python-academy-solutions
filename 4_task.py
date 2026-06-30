n = int(input())
students = {}
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    students[name] = marks

student_name = input()

# Расчет среднего балла для указанного студента
average = sum(students[student_name]) / len(students[student_name])
print(f"{average:.2f}")