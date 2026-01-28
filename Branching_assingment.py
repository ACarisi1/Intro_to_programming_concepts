charge = 0.07633
overCharge = 0.09259

usage = int(input("How many kilowatt hours have you used?: "))

if usage <= 1000:
    cost = usage * charge
    roundedCost = f"{cost:.2f}"
    print("Amount owed:", roundedCost)
else:
    cost = (usage - 1000) *overCharge
    cost = cost + (1000 * charge)
    roundedCost = f"{cost:.2f}"
    print("Amount owed is :", roundedCost)
