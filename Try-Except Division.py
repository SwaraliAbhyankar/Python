a=int(input("Enter 'a' value: "))
b=int(input("Enter 'b' value: "))

try:
    c=a//b
    print(c)
except:
    print("Division by 0 error")

print("End")