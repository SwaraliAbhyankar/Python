import cmath

a = int(input("Enter value of a "))
b = int(input("Enter value of b "))
c = int(input("Enter value of c "))
r1 = (-b + cmath.sqrt(b*b - 4*a*c)) / (2*a)
r2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
print("The roots of the given equation are:",r1,r2)