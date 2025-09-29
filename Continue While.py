count = 0

while count < 10:
    n = int(input("Enter number: "))
    if n % 3 == 0:
        continue
    count += 1
    print(n)
