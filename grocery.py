groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}
shopping_cart = []
while True:
    item = input("What do you want to buy? ")
    if item == "done":
        break
    elif item in groceries:
        shopping_cart.append(item)
    else:
        print("Sorry, we don't have that item.")
total_cost = 0
for item in shopping_cart:
    total_cost += groceries[item]
print("\nYou bought: " + str(shopping_cart) + "\nTotal = $" + str(total_cost))
if total_cost > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")