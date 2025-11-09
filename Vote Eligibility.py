Current_Year = 2025
Birth_Year = int(input("Enter your birth year: "))

Age = Current_Year - Birth_Year

if Age >= 18:
    print("You can vote!")
else:
    print("You cannot vote!")
