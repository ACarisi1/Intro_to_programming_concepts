charge = 0.07633
overCharge = 0.09259

usage = int(input("How many kilowatt hours have you used?: "))

if usage <= 1000:
    cost = usage * charge
    print("Amount owed:", cost)
else:
    cost = (usage - 1000) *overCharge
    print("Amount owed:", cost)
