class Duck:
    def talk(self):
        print('Duck talking')

    def walk(self):
        print('Duck walking')


class Dog:
    def talk(self):
        print('Dog talking')

def Person(pet): 
    pet.talk()
    if hasattr(pet, 'walk'):
        pet.walk()

dog = Dog()
Person(dog)