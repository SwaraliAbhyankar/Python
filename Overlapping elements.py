L1=[5,8,6,4,7,12,15,2]
L2=[3,6,9,7,8,1,4,15,13,28]
L3=[]

for i in L1:
    if i in L2:
        L3.append(i)

print(L3)