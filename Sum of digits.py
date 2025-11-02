n = int(input("Enter a number: "))
Sum = 0

while n > 0:
    r = n % 10
    n = n // 10
    Sum = Sum + r

print("Sum of digits is ", Sum)
