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