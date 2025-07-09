# Indian Restaurant Management System
menu = {
    "Appetizers": {
        1: ("Samosa", 20),
        2: ("Paneer Tikka", 80),
        3: ("Aloo Tikki", 30)
    },
    "Main Course": {
        4: ("Paneer Butter Masala", 150),
        5: ("Chole Bhature", 100),
        6: ("Dal Makhani", 120),
        7: ("Butter Naan", 25)
    },
    "Desserts": {
        8: ("Gulab Jamun", 40),
        9: ("Kheer", 50),
        10: ("Rasgulla", 45)
    },
    "Beverages": {
        11: ("Masala Chai", 15),
        12: ("Lassi", 30)
    }
}

# Flatten the menu to make lookup easy
all_items = {}
for category in menu:
    all_items.update(menu[category])

order = []

print(" Welcome to Daksh's Traditional Indian Restaurant!")
print("-" * 50)
print("Here's our menu:\n")

for category, items in menu.items():
    print(f"\n{category}:")
    for code, (item, price) in items.items():
        print(f"  {code}. {item} - ₹{price}")

print("\nPlease enter the item numbers you wish to order.")
print("Enter 0 when you're done.\n")

# Taking order
while True:
    try:
        choice = int(input("Enter item number: "))
        if choice == 0:
            break
        elif choice in all_items:
            qty = int(input(f"Enter quantity for {all_items[choice][0]}: "))
            order.append((all_items[choice][0], all_items[choice][1], qty))
        else:
            print("Invalid item number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

# Print Bill
if order:
    print("\n Your Bill:")
    print("-" * 40)
    total = 0
    for item, price, qty in order:
        item_total = price * qty
        print(f"{item:<20} ₹{price} x {qty} = ₹{item_total}")
        total += item_total
    print("-" * 40)
    print(f"{'Total Amount':<20} = ₹{total}")
    print(" Thank you for dining with us!")
else:
    print("No items ordered. Visit again soon!")
