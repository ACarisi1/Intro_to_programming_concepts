class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:
    def __init__(self):
        self.beverages = {
            "1": Beverage("Water", 1.0),
            "2": Beverage("Dr Pepper", 1.0),
            "3": Beverage("Coke", 1.0),
            "4": Beverage("Pepsi", 1.0),
            "5": Beverage("Gatorade", 1.0),
            "6": Beverage("Fanta", 1.0)
        }

    def display_menu(self):
        print("\n--- Vending Machine ---")
        for key, drink in self.beverages.items():
            print(key + ".", drink.name, "$" + str(drink.price))

    def process_selection(self):
        choice = input("Select a drink: ")

        if choice not in self.beverages:
            print("Invalid selection.")
            return

        drink = self.beverages[choice]
        print("You selected:", drink.name)

        money = 0.0
        print("Price:", drink.price)
        while money < drink.price:
            more = float(input("Insert money: "))
            money += more
            print("You still owe:", round(drink.price - money, 2))
        if money > drink.price:
            change = money - drink.price
            print("Here is your change:", round(change, 2))

        print("Vending", drink.name, "...\nEnjoy!")

    def run(self):
        self.display_menu()
        while True:
            self.process_selection()



machine = VendingMachine()
machine.run()
