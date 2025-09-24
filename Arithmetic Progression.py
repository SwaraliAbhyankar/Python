a=int(input("Enter first number a: "))
d=int(input("Enter common difference d: "))
n=int(input("Enter number of terms n: "))

for terms in range(a, n*d+a, d):
    print(terms)