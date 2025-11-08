class NegativeDimensionError(Exception):
    def __init__(self):
        self.msg = 'Dimensions you entered are negative'
    def __str__(self):
        return self.msg

def area(length, breadth):
    if length>0 and breadth>0:
        a=length*breadth
        return a
    else:
        raise NegativeDimensionError()
    

print(area(10,-3))