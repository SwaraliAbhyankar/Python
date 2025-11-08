def fun1(*args):
    print(type(args), args)

fun1()
fun1(10,20)
fun1(20,25,30,35,40,45,50,55,60,65,70)
fun1('SAK', 22, 56.25, True, (1+28j))
