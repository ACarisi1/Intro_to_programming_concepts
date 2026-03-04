
menu = {
    "taco": 3,
    "burrito": 7,
    "quesadilla": 6,
    "nachos": 5,
    "drink": 2
}
print(menu)
total = 0.0

print("Welcome to Taco Palace! ")
print("Here is our menu:")


print("\nType the item name to order.")


while True:
    order = input("What would you like to order? ")

    if order == "Q":
        break
    elif order in menu:
        total += menu[order]
        print(f"Added", order,": $",menu[order],":")
        print(f"Current total: $",total,":\n")
    else:
        print("Sorry, we don't have that item.\n")

print(f"\nYour final total is: ${total:.2f}")

