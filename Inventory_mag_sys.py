print("Welcome to the Inventory Management System")

print("Please select an option from the menu")

inventory = {}

def add_item():
    item_name = input("Enter the item name: ").strip() # Strip Removes accidental spaces
    item_quantity = int(input("Enter the item quantity: "))
    item_price = float(input("Enter the item price per unit: "))
    if item_name in inventory:
        inventory[item_name]['quantity'] += item_quantity
    else:
        inventory[item_name] = {'quantity': item_quantity, 'price': item_price}
    
    print(f"{item_name} added.")
    # print(inventory)


def remove_item():
    item_name = input("Enter the item name to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed.")
    else:
        print(f"{item_name} not found in inventory.")
def update_item():
    item_name = input("Enter the item name to update: ")

    if item_name in inventory:
        try:
            new_quantity = int(input("Enter the new quantity: "))
            new_price = int(input("Enter the new price per unit: "))
            inventory[item_name]['quantity'] = new_quantity
            inventory[item_name]['price'] = new_price
            print(f"{item_name} updated.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the quantity.")
    else:
        print(f"{item_name} not found in inventory.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for item, details in inventory.items():
            print(f"{item}: {details['quantity']} units at ₹{details['price']} per unit")
    # print(inventory)

def exit_program():
    print("Exiting the program...\nGoodbye!")
    exit()

while True:
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Update item in inventory")
    print("4. View inventory")
    print("5. Exit")


    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        update_item()
    elif choice == 4:
        view_inventory()
    elif choice == 5:
        exit_program()
    else:
        print("Invalid choice. Please try again.")