def fun(**kwargs):
    for item in kwargs.items():
        if item[0] == 'b':
            print(item[1])

fun(a=5, b=10, c=15)