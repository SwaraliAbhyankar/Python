s1=input("Enter 1st string: ")
s2=input("Enter 2nd string: ")

if len(s1) != len(s2):
    print("String lengths doesn't match.")
    print("Not anagram")
else:

    for x in s1:
        if x not in s2:
            print("Not anagram")
            break
    else:
        print("Anagram")
