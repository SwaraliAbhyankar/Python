def weekdays():
    days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    i=0

    while True:
        yield days[i]
        i = (i+1) % 7

d=weekdays()

print(next(d))
print(next(d))
print(next(d))