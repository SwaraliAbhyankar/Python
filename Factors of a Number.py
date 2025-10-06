n=int(input("Enter a number: "))
count=1

print("Factors of",n,'are:')
for i in range(1, n+1):
    if n % i == 0:
        print(i)
