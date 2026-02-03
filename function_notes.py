def printMessage():
    print("I don't return a value")

def printMessage2(value1, value2):
    ans = value1 + value2
    return ans

answer = printMessage2(4, 2)
print(answer)
printMessage()

def sum(value1, value2):
    ans = value1 + value2
    return ans
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
answer2 = sum(num1, num2)
print(answer2)

#create a function that will take one parameter
#it will convert the argument for the parameter and create the
#next number in a sequence by multiplying it by 2 and adding 3
#retrun that number and print it to the screen
def convert(value1):
    ans = (value1 * 2) + 3
    return num

num = int(input("Enter first number: "))
ans2 = convert(num)
print(ans2)


