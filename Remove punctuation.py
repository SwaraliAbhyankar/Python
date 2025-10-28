s1 = input("Enter string: ")

punc = ''
s2=''

for x in s1:
    if x.isalnum():
        punc += x

print("Modified string: ",s2+punc)

#Same Prog can also be done by mentioning all punctuations and using 'not in'.
#This is shown in Punctuation.py
