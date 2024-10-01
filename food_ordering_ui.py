import data
import functions

def show_main_menu():
    while True:
        print("Keerthana Sai Avisana")
        print("__________")
        print('N for a new order')
        print('X for close orders and print the check')
        print('M for manager options')
        print('Q for quit')
        user_menu_choice = input('Your choice: ').upper()
        
        if user_menu_choice == 'Q':
            break
        elif user_menu_choice == 'X':
            close_order(user_menu_choice)
        elif user_menu_choice == 'N':
            make_order(user_menu_choice)
        elif user_menu_choice == 'M':
            show_manager_menu()
        else:
            print("Invalid choice. Please choose N, X, M, or Q.")

def make_order(menu_choice):
    print('Functionality for menu choice', menu_choice)
    
    orders = []  # List to store items for the current order
    
    while True:
        # Get the customer input for item and quantity
        user_selection = input("Enter item code and quantity (e.g., '30 BURGER'): ").upper()
        
        try:
            # Split the input into quantity and item code
            quantity, item_code = user_selection.split()
            quantity = int(quantity)  # Ensure quantity is a valid integer
        except ValueError:
            print("Invalid input format. Please enter in the format 'quantity ITEM_CODE'.")
            continue
        
        # Verify if the item is on the menu
        item_name, item_price, stock = functions.get_item_information(item_code)
        
        if item_name:
            print(f"Item found: {item_name}, Unit Price: ${item_price:.2f}, Stock: {stock}")
            
            # Check if the requested quantity is available
            if stock == "Unlimited" or quantity <= stock:
                total_price = item_price * quantity
                orders.append((item_name, quantity, total_price))
                
                # Update the stock
                if stock != "Unlimited":
                    for item in data.menu_items_dict:
                        if item['code'] == item_code:
                            item['stock'] -= quantity
                            break
                
                print(f"Order confirmed: {quantity} x {item_name}, Total Price: ${total_price:.2f}")
            else:
                print(f"Sorry, only {stock} units of {item_name} are available.")
        else:
            print("Invalid item code. Please try again.")
        
        more_items = input("Add more items? (Y/N): ").upper()
        if more_items != 'Y':
            break

    print(f"Order Summary: {orders}")

def close_order(menu_choice):
    print('Functionality for menu choice', menu_choice)
    # Print the list of items ordered, extended price, total, taxes, and grand total
    # To be implemented with more detailed calculations

def show_manager_menu():
    while True:
        print("\nManager Options")
        print("1. Add a new menu item")
        print("2. Remove a menu item")
        print("3. Update a menu item (Price or Description)")
        print("4. View menu")
        print("Q. Quit to main menu")
        
        manager_choice = input("Your choice: ").upper()
        
        if manager_choice == '1':
            add_menu_item()
        elif manager_choice == '2':
            remove_menu_item()
        elif manager_choice == '3':
            update_menu_item()
        elif manager_choice == '4':
            view_menu()
        elif manager_choice == 'Q':
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or Q.")

def add_menu_item():
    code = input("Enter item code (e.g., E5): ").upper()
    name = input("Enter item name (e.g., PIZZA): ").upper().replace(" ", "_")
    price = float(input("Enter item price: "))
    stock = int(input("Enter item stock: "))
    
    # Add the new item to the menu_items_dict
    new_item = {
        'code': code,
        'name': name,
        'price': price,
        'stock': stock
    }
    
    data.menu_items_dict.append(new_item)
    print(f"Item {name} added to the menu.")

def remove_menu_item():
    code = input("Enter the item code to remove (e.g., E1): ").upper()
    
    # Remove the item from the menu_items_dict
    for item in data.menu_items_dict:
        if item['code'] == code:
            data.menu_items_dict.remove(item)
            print(f"Item {item['name']} removed from the menu.")
            return
    
    print("Item code not found.")

def update_menu_item():
    code = input("Enter the item code to update (e.g., E1): ").upper()
    
    # Find the item in the menu and update its information
    for item in data.menu_items_dict:
        if item['code'] == code:
            print(f"Current details: Name: {item['name']}, Price: {item['price']}, Stock: {item.get('stock', 'Unlimited')}")
            choice = input("Do you want to update Price (P), Description (D), or both (B)? ").upper()
            
            if choice in ['P', 'B']:
                new_price = float(input(f"Enter new price for {item['name']}: "))
                item['price'] = new_price
                print(f"Price updated to {new_price}.")
                
            if choice in ['D', 'B']:
                new_name = input(f"Enter new description for {item['name']}: ").upper().replace(" ", "_")
                item['name'] = new_name
                print(f"Description updated to {new_name}.")
            
            return
    
    print("Item code not found.")

def view_menu():
    print("\nCurrent Menu:")
    for item in data.menu_items_dict:
        stock_info = item.get('stock', 'Unlimited')
        print(f"Code: {item['code']}, Name: {item['name']}, Price: ${item['price']:.2f}, Stock: {stock_info}")
    print("\n")

if __name__ == '__main__':
    show_main_menu()
