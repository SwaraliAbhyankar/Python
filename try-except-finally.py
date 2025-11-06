def f():
    try:
        x=int('2801')
        return x
    except Exception as e:
        raise e
    finally:
        print('End of function')

res=f()
print(res)