Swara=['pizza','burger','fries','noodles','hotdog','pasta']
Anuj=['fries','pasta','pizza','hotdog','noodles','burger']

S_index=10
A_index=10

for i in range(len(Swara)):
    common_index=Anuj.index(Swara[i])      #finding matching index of same item in Anuj

    if i + common_index < S_index + A_index:
        S_index = i
        A_index = common_index

print("Common fav item: ", Swara[S_index], S_index+A_index)
