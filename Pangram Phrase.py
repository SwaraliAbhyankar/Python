def pangram(phrase):
    letter = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
              't','u','v','w','x','y','z',' '}
    
    phr = set(phrase)

    if len(phr) >= len (letter):    #if phr >= letters:
        return True
    else:
        return False    #instead of if..else can write: return phr >= letter
    

p = input("Enter a phrase: ")
P=pangram(p)
print(P)