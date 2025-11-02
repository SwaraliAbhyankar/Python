import Student, pickle

studs = [Student.Student(1, 'Swarali', 'Physics'), Student.Student(2, 'Anuj', 'CSE'),
       Student.Student(3, 'Khare', 'MCA')]

with open('Students.data', 'wb') as f:
    for s in studs:
        pickle.dump(s,f)