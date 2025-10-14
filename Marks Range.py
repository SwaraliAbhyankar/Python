marks = int(input("Enter marks: "))
total_marks = 150
percentage: float = marks / total_marks * 100

if 0 <= marks <= 150:
    print('Valid marks')
    print('Percentage = ',percentage,'%')
else:
    print('Invalid marks')
