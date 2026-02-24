print("--- Grocery Store Billing System ---")

total_cost = 0

for i in range(1, 6):
    print(f"\nItem #{i}:")
    
    item_name = input("Enter item name: ")
    price = float(input("Enter price: Rs. "))
    quantity = int(input("Enter quantity: "))
    
    item_total = price * quantity
    print(f"Subtotal for {item_name}: Rs. {item_total}")
    
    total_cost = total_cost + item_total

discount = 0

if total_cost > 100:
    discount = total_cost * 0.10

final_payable = total_cost - discount

print("\n      BILLING SUMMARY      ")
print("Original Total: Rs.", total_cost)
print("Discount Applied: Rs.", discount)
print("Final Amount: Rs.", final_payable)
print("Thank you for shopping!")