L1=['A','B','C','D','E','A','D','C','A','E','B','C','E']
result=[]

for x in L1:
    if x not in result:
        result.append(x)
        count=L1.count(x)
        result.append(count)

print(result)