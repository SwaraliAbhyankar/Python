pswd1 = input("Enter password: ")
pswd2 = input("Confirm password: ")

if pswd1 == pswd2:
    print("Password confirmed!")
elif pswd1.casefold() == pswd2.casefold(): 
    print("Passwords match, cases don't!. Check the cases again")
else:
    print("Incorrect password")
    