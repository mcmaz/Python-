def salaryslip (name, salary):
    if salary>=2000:
        tax=salary*20/100
    else:
        tax=salary*15/100
    netsalary=salary-tax
    print("Name of employee", name)
    print("Current salary", salary)
    print("Tax", tax)
    print ("Net Salary", netsalary)

salaryslip("Marianne", 3000)

