s1=input("Enter a string: ")

lower=''
upper=''
num=''

for x in s1:
    if x.islower():
        lower += x
    elif x.isupper():
        upper += x
    else:
        num += x

s2=lower+upper+num

print("Rearranged string: ", s2)
