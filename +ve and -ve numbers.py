num_of_nos = int(input("Enter number of numbers: "))
pos_sum = 0
count = 0
neg_sum = 0

while count < num_of_nos:
    n = int(input("Enter a number: "))
    if n > 0:
        pos_sum = pos_sum + n
    else:
        neg_sum = neg_sum + n
    count += 1

Total_Sum = pos_sum + neg_sum

print("Sum of positive numbers is: ", pos_sum)
print("Sum of negative numbers is: ", neg_sum)

print("Sum of numbers is: ", Total_Sum)
