print("Bill Split Calculator")
bill = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage:"))
guests = int(input("Enter the number of guests:"))
real_tip = (tip_percentage / 100) * bill
total_bill = bill + real_tip
split = bill / guests
print(f"Total bill including tip: ${total_bill:.2f}")
print(f"Each guest should pay: ${split:.2f}")