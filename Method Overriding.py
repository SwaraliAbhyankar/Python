class Parent:
    def show(self):
        print('Parent show')

class Child(Parent):
    #pass
    def show(self):
        print('Child show')

c = Child()
c.show()