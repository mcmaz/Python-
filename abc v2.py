product=input("Product purchased:")
quantity=input("How much do you need?")
price=input("How much does it cost?")
bill=int(quantity)*float(price)
print()
print()
print("--------------------")
print("TOTAL INVOICE")
print("Product:",product)
print("Amount purchased:",quantity)
print("Price",price)
print("TOTAL",bill)



temp=input("enter today's temp")
if float (temp)>40:
    print("it is hot")
if float (temp)<40:
    print("it is cold")
if temp==40:
    print("Nice weather")


salary=int(input("Enter your salary"))
if salary>2000:
    tax=salary*20/100
    net=salary-tax
if salary<2000:
    tax=salary*10/100
    net=salary-tax
print("Tax", tax)
print("Net salary", net)
