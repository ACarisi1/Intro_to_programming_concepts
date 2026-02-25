def call():
    print("Welcome to Taco Palace!  Please view the menu below and make a selection\n"
          "1 for taco\n"
          "2 for nacho\n"
          "3 for burrito\n"
          "4 for drink\n"
          "5 to quit")
def taco():
    taco_price = 3
    order.append("Taco")
    cost.append(taco_price)
    print("Your have selected a Taco")

def nachos():
    nacho_price = 2
    order.append("Nacho")
    cost.append(nacho_price)
    print("Your have selected the Nachos")

def burrito():
    burrito_price = 4
    order.append("Burrito")
    cost.append(burrito_price)
    print("Your have selected a Burrito")

def drink():
    drink_price = 1
    order.append("Drink")
    cost.append(drink_price)
    print("Your have selected a Drink")

continueLoop = True
order = []
cost = []

call()
while continueLoop:
    total = sum(cost)
    userInt = int(input("Enter a number to place your order: "))
    if userInt == 1:
        taco()
    elif userInt == 2:
        nachos()
    elif userInt == 3:
        burrito()
    elif userInt == 4:
        drink()
    else:
        print("Here is your order: ", order)
        print("The cost is: ",total, "dollars")
        continueLoop = False
