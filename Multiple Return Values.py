def fun3(a, b, c):
    return a+1, b+1, c+1

x, y, z = fun3(3,4,5)   #unpacking by giving in different variables
t = fun3(7,8,9)     #unpacking in the form of a tuple by giving in single variable

print(x,y,z)
print(t)