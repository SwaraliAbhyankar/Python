def fun2(a, b, c):
    print(a,b,c)

L1=[11,22,33]
T1=(10,20,30)
str1='SAK'
set1={21,55,12}

fun2(L1[0], L1[1], L1[2])   # fun2(*L1)
fun2(*T1)
fun2(*str1)
fun2(*set1)