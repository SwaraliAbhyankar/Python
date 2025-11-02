students={}

for i in range(3):
    name = input("Enter name: ")
    roll_no = int(input("Enter roll number: "))
    dept = input("Enter department: ")

    students[name] = {'Name':name,'Roll No':roll_no, 'Department':dept }

print(students)