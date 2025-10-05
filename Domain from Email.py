email = input("Enter email id: ")

atrate = email.find("@")

user_id = email[0:atrate]
domain = email[atrate+1::]

print("User name: ", user_id)
print('Domain: ', domain)
