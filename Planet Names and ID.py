def planet(id):
    Planet = {1:'Mercury', 2:'Venus', 3:'Earth', 4:'Mars', 5:'Jupiter', 6:'Saturn', 
              7:'Uranus', 8:'Neptune', 9:'Pluto'}
    
    return Planet[id]

id = int(input("Enter ID of a planet: "))

p = planet(id)
print('Planet:',p)