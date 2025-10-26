punc = '''!()-_[]{};:'"\,<>./?@#$%^&*~'''

s1=input("Enter string: ")

s2=''

for x in s1:
    if x not in punc:
        s2 = s2 + x

print("Modified string: ",s2)
