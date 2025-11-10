name = str(input("Enter full name: "))
Age = int(input("Enter your age: "))

print(name)

if not(18 <= Age <= 60):
    print("Not eligible")
else:
    print("Eligible")
