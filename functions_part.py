delectable_menu = [
    ["Hamburger", 5.99],
    ["Cheeseburger", 7.99],
    ["Chicken Nuggets", 5.99],
    ["Farmer's Salad", 9.99],
    ["Apple Salad", 8.99],
    ["French Fries", 3.99],
    ["Potato Wedges", 4.99],
    ["Hash Browns", 4.50],
    ["Side Salad", 3.99],
    ["Chocolate Shake Dream", 6.99],
    ["Vanilla Shake Pudding", 6.99],
    ["Strawberry Fields Shake", 6.99],
    ["Water", 0.50],
    ["Sparkling Water", 1.50],
    ["Apple Juice", 2.00],
    ["Orange Juice", 2.00],
    ["Coke", 2.50],
    ["Sprite", 2.50]
]

def display_menu():
    print("\n--- MENU ---")
    # Loop through the list to show number, name, and price
    for i in range(len(delectable_menu)):
        item = delectable_menu[i]
        print(f"{i + 1}. {item[0]} - {item[1]} EUR")

def take_order():
    display_menu()
    order = [] # This list will store the user's choices
    
    while True:
        choice = input("\nEnter the item number (or '0' to finish): ")
        
        if choice == '0':
            break
            
        # Convert input string to an integer index
        index = int(choice) - 1 
        item = delectable_menu[index]
        
        # Ask for the quantity of the selected item
        qty = int(input(f"How many '{item[0]}' would you like? "))
        
        # Store item details: [Name, Unit Price, Quantity]
        order.append([item[0], item[1], qty])
        print("Added to cart!")
            
    return order

def calculate_final_bill(order):
    print("\n--- YOUR RECEIPT ---")
    total = 0
    
    # Process each item in the order list
    for row in order:
        name = row[0]
        price = row[1]
        qty = row[2]
        
        # Calculate cost for this specific item
        cost = price * qty
        total = total + cost
        print(f"{name}: {qty} x {price} = {cost:.2f} EUR")
    
    # Show the final total cost
    print(f"TOTAL TO PAY: {total:.2f} EUR")
    print("Thank you for your visit!")

# Start the program execution
my_order = take_order()
calculate_final_bill(my_order)