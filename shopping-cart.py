basket = []
price = []
print("-"*80)
print("Welcome to the General Store!")
print("-"*80 + "\n")
print("To start shopping, please choose from the following menu -")
print("1. Add an item to your cart")
print("2. Remove an item from your cart")
print("3. See the total cost of the items in your basket")
print("4. Checkout and finish shopping\n")
user_choice = input("Choose an option to continue: ")
if user_choice == "1":
    new_item = input("Enter the name of the item being purchased: ")
    basket.append(new_item)
    new_price = input("Enter the value of the item in GBP: ")
    