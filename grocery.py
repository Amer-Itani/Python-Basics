groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}
shopping_cart = []
cart = {}
while True:
    item_quantity = input("What do you want to buy and how many? ").split()
    item = item_quantity[0]
    if item == "done":
        break
    elif len(item_quantity) !=2:
        print("Please enter item and quantity respectively seperated by a whitespace.")
    elif item not in groceries:
        print("Sorry, we don't have that item.")
    else:
        quantity = int(item_quantity[1])
        shopping_cart.append(item)
        cart[item] = quantity
total_cost = 0
for item in shopping_cart:
    total_cost += groceries[item] * cart[item]
if "milk" in cart:
    if cart["milk"] > 2:
        total_cost -= 1
print("\nYou bought: " + str(shopping_cart) + "\nTotal = $" + str(total_cost))
if total_cost > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")