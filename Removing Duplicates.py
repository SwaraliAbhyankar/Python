L1=[3,6,3,4,3,2,5,4,7,5,3,6,5,4,8,5,6,2,5]
L2=[]

for x in L1:
    if x not in L2:
        L2.append(x)

L2 = sorted(L2)
print(L2)