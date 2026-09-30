amount = float(input("Enter total purchase amount: $"))
status = input("Enter loyalty status (Regular or Premium): ")

if amount > 1000:
    if status == "Premium":
        discount_rate = 0.20
    else:
        discount_rate = 0.10
elif amount >= 500:
    if status == "Premium":
        discount_rate = 0.15
    else:
        discount_rate = 0.05
else:
    if status == "Premium":
        discount_rate = 0.10
    else:
        discount_rate = 0.02

discount = amount * discount_rate
final_amount = amount - discount

print(f"Discounted amount: ${discount:.2f}")
print(f"Final amount to pay: ${final_amount:.2f}")