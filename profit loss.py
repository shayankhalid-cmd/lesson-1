h = float(input("enter price of product here:"))
y = float(input("enter sales price of product here:"))
if y>h:
    profit = y - h 
    print (profit,"is the total profit")
else:
    print ("no profit")