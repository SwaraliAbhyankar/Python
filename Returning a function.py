def Outer():
    def Inner():
        print('Welcome')

    return Inner

f=Outer()
f()