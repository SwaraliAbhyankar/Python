codes=['._', '_..', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', 
       '._..', '__', '_.', '___', ',__.', '__._', '._.', '...', '_', '.._', '..._', 
       '.__', '_.._', '_.__', '__..']
text=input("Enter text in lower case: ")

morse_code=''

for x in text:
    morse_code += codes[ord(x)-ord('a')] + '  '

print(morse_code)