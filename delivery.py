import os
from reserved import getName, getContact, getAddress

filename = "foodOrder.txt"
cancelCall = False

# Check if the file exists
if not os.path.exists(filename):
    # If it doesn't exist, create it
    with open(filename, "w") as file:
        pass  # The "pass" keyword does nothing, but it's necessary here because an empty block is not allowed in Python

def showMenu():
    print("""Appetizers:\nA1\tBacon-Wrapped Dates with Balsamic Glaze
A2\tPesto and Sundried Tomato Bruchetta
A3\tSpinach and Artichoke Dip with Naan Bread\n
Mains:\nM1\tKorean BBQ Beef Tacos with Slaw
M2\tChicken and Waffles with Spicy Maple Syrup
M3\tSalmon with Mango Salsa and Cilantro Rice\n
Desserts:\nD1\tChocolate Chip Cookie Skillet with Vanilla Ice Cream
D2\tBerry and Mascarpone Tart
D3\tMatcha Green Tea Tiramisu\n
Beverages:\nB1\tMango Lassi
B2\tRaspberry Lemonade
B3\tPeach Bellini""")

def foodOrder():
    # Initialize an empty list to store the user's food order
    foodOrder = []
    global cancelCall

    # Prompt the user to enter their food order
    while True:
        order = input("Enter the code of the dish you'd like to order (or 'done' to finish): ")

        # Check if the user is finished ordering
        if order.lower() == "done":
            print(f"Your order:\n{foodOrder}")
            break

        if order.lower() == 'cancel':
            cancelCall = True
            break

        # Map the user's input to the corresponding dish in the menu
        if order == "A1":
            dish = "Bacon-Wrapped Dates with Balsamic Glaze"
            print(f'added 1 {dish}')
        elif order == "A2":
            dish = "Pesto and Sundried Tomato Bruschetta"
            print(f'added 1 {dish}')
        elif order == "A3":
            dish = "Spinach and Artichoke Dip with Naan Bread"
            print(f'added 1 {dish}')
        elif order == "M1":
            dish = "Korean BBQ Beef Tacos with Slaw"
            print(f'added 1 {dish}')
        elif order == "M2":
            dish = "Chicken and Waffles with Spicy Maple Syrup"
            print(f'added 1 {dish}')
        elif order == "M3":
            dish = "Salmon with Mango Salsa and Cilantro Rice"
            print(f'added 1 {dish}')
        elif order == "D1":
            dish = "Chocolate Chip Cookie Skillet with Vanilla Ice Cream"
            print(f'added 1 {dish}')
        elif order == "D2":
            dish = "Berry and Mascarpone Tart"
            print(f'added 1 {dish}')
        elif order == "D3":
            dish = "Matcha Green Tea Tiramisu"
            print(f'added 1 {dish}')
        elif order == "B1":
            dish = "Mango Lassi"
            print(f'added 1 {dish}')
        elif order == "B2":
            dish = "Raspberry Lemonade"
            print(f'added 1 {dish}')
        elif order == "B3":
            dish = "Peach Bellini"
            print(f'added 1 {dish}')
        else:
            print("Invalid input. Please enter the code infront of the food.")
            continue

        # Add the dish to the food order list
        foodOrder.append(dish)
    return foodOrder

def save(name: str, contactNum: str, address, order):
    # Open the text file in "append" mode and write the user's information to it
    with open(filename, "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Contact Number: {contactNum}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Order:\n")
        for dish in order:
            file.write(dish + "\n")
        file.write(f"\n")

    print("Your order has been send to the kitchen")

# Open file in write mode and save food order to it
def delivery():
    global cancelCall
    showMenu()
    order = foodOrder()
    if cancelCall == True:
        print("Okay, action cancelled.")
        cancelCall = False
        return 0
    name = getName()
    contact = getContact()
    address = getAddress()
    save(name, contact, address, order)
