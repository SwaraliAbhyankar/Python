def result(mrk1, mrk2, mrk3):

    total = mrk1+mrk2+mrk3

    average = total / 3
    
    if average >= 45:
        grade='Pass'
    else:
        grade='Fail'

    return total, average, grade

Result = result(67,55,79)

print('Result:', Result)