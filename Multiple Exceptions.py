L=[10,20,30,40,50]

try:
    index=int('abc')
    print(L[index])
except IndexError:
    print('Invalid index')
except TypeError:
    print('Index should be integer')
except:
    print('Error')

print('End of program')