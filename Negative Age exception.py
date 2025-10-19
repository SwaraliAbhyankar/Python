class NegativeAgeError(Exception):
    def __init__(self):
        self.msg = 'You entered negative age number'
    def __str__(self):
        return self.msg
    
def stage(age):
    if 0 < age < 13:
        print('Kid')
    elif 13<= age <=19:
        print('Teen')
    elif 19< age <=50:
        print('Adult')
    elif age >50:
        print('Old')
    else:
        raise NegativeAgeError
    
age = int(input('Enter your age: '))

try:
    stage(age)
except NegativeAgeError as n:
    print(n)