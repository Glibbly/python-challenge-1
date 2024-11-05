
#A DISCLAIMER, i spent hours tweaking this and using an AI assistant to help me fix my errors on this so it will
#look slightly different in format to the original homework. Please let me know if there are any issues. Thank you

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit() and int(menu_category) in menu_items.keys():
        # Save the menu category name to a variable
        menu_category_name = menu_items[int(menu_category)]
        print(f"\nYou selected {menu_category_name}")

        # Print out the items in the selected category
        i = 1
        menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            if type(value) is dict:
                for key2, value2 in value.items():
                    num_item_spaces = 24 - len(key + key2) - 3
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                    menu_items[i] = {
                        "Item name": key + " - " + key2,
                        "Price": value2
                    }
                    i += 1
            else:
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value}")
                menu_items[i] = {
                    "Item name": key,
                    "Price": value
                }
                i += 1

        # Ask customer to input menu item number
        menu_selection = input("\nPlease select a menu item number: ")

        if menu_selection.isdigit() and int(menu_selection) in menu_items:
            menu_selection = int(menu_selection)
            item_name = menu_items[menu_selection]['Item name']
            item_price = menu_items[menu_selection]['Price']
            
            # Ask the customer for the quantity of the menu item
            quantity_input = input(f"How many {item_name} would you like to order? ")
            quantity = int(quantity_input) if quantity_input.isdigit() else 1
            if not quantity_input.isdigit():
                print("Invalid quantity. Defaulting to 1.")

            # Add the item to the order list
            order_list.append({
                'Item': item_name,
                'Price': item_price,
                'Quantity': quantity
            })
            print(f"\nAdded {quantity} x {item_name} to your order.")
        else:
            print("You did not select a valid menu item.")

    else:
        print("You did not select a valid menu category.")

    # Ask if they want to keep ordering
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()
    if keep_ordering == 'n':
        place_order = False

# Print the final order summary
print("\nThis is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
total_cost = 0
for item in order_list:
    item_name = item['Item']
    item_price = item['Price']
    quantity = item['Quantity']
    
    item_name_spaces = 24 - len(item_name)
    price_spaces = 7 - len(f"{item_price:.2f}")
    
    item_name_space_str = " " * item_name_spaces
    price_space_str = " " * price_spaces
    
    print(f"{item_name}{item_name_space_str} | ${item_price:.2f}{price_space_str} | {quantity}")
    ## Calculate the cost of the order using list comprehension
    total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)
    print("\nTotal cost of your order: ${:.2f}".format(total_cost))
    print("\nThank you for ordering from our food truck!")

