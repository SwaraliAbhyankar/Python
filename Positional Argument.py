def net_sal(basic, allowance, deduction):
    print('Basic:',basic)
    print('Allowance:',allowance)
    print('Deduction:',deduction)
    net = basic+allowance-deduction        # Gross salary=basic+allowance
    return net

salary = net_sal(15000,3000,7000)

print('Salary:',salary)