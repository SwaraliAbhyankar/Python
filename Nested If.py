Alex = int(input("Alex age: "))
Brian = int(input("Brian age: "))
Chandler = int(input("Chandler age: "))

if Alex > Brian and Alex > Chandler:
    print("Alex is the eldest")
else:
    if Brian > Chandler:
        print("Brian is the eldest")
    else:
        print("Chandler is the eldest")
