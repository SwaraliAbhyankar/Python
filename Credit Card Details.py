card_no = input("Enter 16 digit card no - ")

last4dig = card_no[15::]
star = '*' * 4 + ' '

disp_no = star * 3 + last4dig
print(disp_no)
