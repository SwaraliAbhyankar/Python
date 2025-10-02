date = input('Enter date: ')

slash1 = date.find('/')
slash2 = date.rfind('/')
#print(slash)

dd=date[:slash1]
mm=date[slash1+1:slash2]
yyyy=date[slash2+1:]

print('Date: ', dd)
print("Month: ", mm)
print("Year: ", yyyy)

# ABOVE CODE IS BY MY UNDERSTANDING
# OTHER CODDE FOR SAME PROG IS IN Date Format.py BY SIR
