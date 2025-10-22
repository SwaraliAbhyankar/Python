class Rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    @property
    def length(self):
        return self._length  #for property method we use _
    
    @length.setter
    def length(self, l): #set_length validates the data
        if l >= 0:
            self._length = l
        else:
            self._length = 1 #_ means protected


r = Rectangle(10,5)
r.length = -9
print(r.length)