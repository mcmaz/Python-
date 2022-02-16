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
else:
    tax=salary*10/100

net=salary-tax

print("Tax", tax)
print("Net salary", net)




salary = int(input("Enter your salary"))
if salary>=1000:
    if salary>=2000:
        tax=salary*25/100
    else:
        tax=salary*15/100
else:
    tax=0
net=salary-tax
print("Tax:", tax)
print("Net salary:", net)


number=int(input("Enter your number"))
if number>1000:
    print("A")
    if number>2000:
        print("C")
        if number>3000:
            print("H")
        print("M")
    print("N")
    else:
        print("D")
        if number>1500:
            print ("J")
        else:
            print ("I")
        print("L")
    print("H")
else:
    print("B")

    if number>500:
        print ("E")
    else:
        print("F")
    print("k")
print("I")
print ("O")
print ("P")






a=1
while a<=10
    print("hello")
    a=a+1

