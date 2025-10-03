L1=[3,6,3,4,3,2,5,4,7,5,3,6,5,4,8,5,6,2,5]

for x in range(len(L1)-1,-1,-1):
    if L1[x] in L1[:x]:
        L1.pop(x)

print(L1)