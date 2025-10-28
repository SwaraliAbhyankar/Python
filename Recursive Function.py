def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1
    
number = int(input("Enter a number: "))

Factorial = fact(number)

print(Factorial)