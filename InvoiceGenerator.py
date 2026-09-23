print("=======================")
print(" INVOICE GENERATOR")
print("=======================")

customer_name = input("Enter customer name: ")

items = []

while True:
    item_name = input("\nEnter item name: ")

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = quantity * price

    items.append([item_name, quantity, price, total])

    more = input("Add another item? (y/n): ").lower()

    if more != "y":
        break

# Calculate subtotal
subtotal = sum(item[3] for item in items)

print("\n=========")
print(" INVOICE")
print("===========")

print(f"Customer: {customer_name}")
print("--------------------")

print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Total'}")
print("--------------------")

for item in items:
    print(f"{item[0]:<15}{item[1]:<8}{item[2]:<10.2f}{item[3]:.2f}")

print("---------------------------")
print(f"Subtotal:     ₹{subtotal:.2f}")
print(f"Grand Total:    ₹{subtotal:.2f}")

print("===========================")
print(" Thank You For Shopping!")
print("============================")