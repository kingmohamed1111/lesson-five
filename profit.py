actual_cost=float(input("Enter the actual cost: "))
sale_amount=float(input("pls enter the sales amount: "))
if sale_amount > actual_cost:
    amount=sale_amount- actual_cost
    print("Total profit  ={0}".format(amount))
else:
    print("no prfit")