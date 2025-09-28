def Outer(msg):
    def Inner():
        print('*'*10)
        print(msg)
        print('*'*10)

    return Inner

f=Outer('Welcome')
f()