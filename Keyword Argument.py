def net_sal(basic, allowance, deduction):
    print('Basic:',basic)
    print('Allowance:',allowance)
    print('Deduction:',deduction)
    net = basic+allowance-deduction        # Gross salary=basic+allowance
    return net

salary = net_sal(basic=15000, allowance=3000, deduction=1000)

print('Salary:',salary)