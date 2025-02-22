def calculate_due_amount(total_bill, amount_paid):
    if amount_paid > total_bill:
        print("Error: Amount paid exceeds total bill.")
        return 0
    
    due_amount = total_bill - amount_paid
    return due_amount

total_bill = float(input("Enter the total bill amount:"))
amount_paid = float(input("Enter the amount paid: "))

due_amount = calculate_due_amount(total_bill, amount_paid)
print(f"Remaining due amount: ${due_amount:.2f}")
