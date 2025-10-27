def div(a,b):
    if b!=0:
        c=a//b
        return c
    else:
        raise ZeroDivisionError
    
try:
    res=div(10,0)
    print(res)
except:
    print('Division by zero error!')