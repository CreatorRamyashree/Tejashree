actual_cost= float(input("Please enter the actual cost of the product: "))
sale_amount= float(input("Please enter the sales amount: "))

if sale_amount>actual_cost:
    amount= sale_amount - actual_cost
    print((amount))

else:
    print("No Profit!!!")









