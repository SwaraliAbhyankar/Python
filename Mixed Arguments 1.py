def add(a,b,/,c,d,e,f):
    print(a,b,c,d,e,f)
    return a+b+c+d+e+f

r = add(2, 5, e=8, f=3, c=9, d=4)
print(r)