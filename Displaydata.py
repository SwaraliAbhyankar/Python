Item_name=input("Enter the item: ")
price = input('Enter the price: ')

total_len = len(Item_name) + len(price)
print(total_len)

dots = '.' * (25-total_len)

print(Item_name + dots + price)
