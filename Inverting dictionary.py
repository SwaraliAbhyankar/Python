def invert(d):
    D={}

    for key, value in d.items():
        D[value] = key

    return D

d1 = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}

d2 = invert(d1)

print("Before: ",d1)
print('After: ',d2)