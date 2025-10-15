no_of_nos = int(input("Enter number of numbers: "))
count = 0
max = int(input("Enter number: "))

while count < no_of_nos - 1:
    n = int(input("Enter a number: "))
    if n > max:
        max = n
    count += 1

print("The maximum of numbers is: ", max)