P = eval(input("Enter principal amount:"))
R = eval(input("Enter rate of interest:"))
T = eval(input("Enter time period in years:"))

CI = P*(1+(R/100)**T) - P
amt = P + CI

print("Compound Interest:",CI)
print('Amount:', amt)