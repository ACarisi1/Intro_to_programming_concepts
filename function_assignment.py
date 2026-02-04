def areaCircle(pi,r):
    area = pi * r**2
    area = round(area,2)
    return area


def taxComputation(money, tax):
    total = money + (money * tax)
    total = round(total,2)
    return total


def convertTemp(fahrenheit):
    temp = (fahrenheit - 32) * 5 / 9
    temp = round(temp,4)
    return temp

pi = 3.14159
r = int(input("Enter the radius: "))
areaCircle(pi,r)
print(areaCircle(pi,r))

money = int(input("Enter the money: "))
tax = float(input("Enter the tax rate: "))
taxComputation(money,tax)
print(taxComputation(money,tax))

fahrenheit = int(input("Enter the temperature in fahrenheit: "))
convertTemp(fahrenheit)
print(convertTemp(fahrenheit))

