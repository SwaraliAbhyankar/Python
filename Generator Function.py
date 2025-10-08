def myrange(n):
    i=0

    while i<n:
        yield i
        i = i+1

m=myrange(5)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
