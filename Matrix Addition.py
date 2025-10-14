L1=[[1,2,3],[1,2,3],[1,2,3]]
L2=[[4,5,6],[4,5,6],[4,5,6]]

L3=[]

for i in range(3):
    Sum=[]
    for j in range(3):
        r= L1[i][j] + L2[i][j]
        Sum.append(r)
    L3.append(Sum)

print(L3)