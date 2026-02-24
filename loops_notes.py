#Structure of a while loop
#while(condition)
    #some code
    #run if the condition is true
    #break this loop if teh condition is false
    #anything that is indented belongs to the while loop
    #the while loop contains the keyword "while" and has a colon at the end
#code that is not in the while loop will run after the while loop ends

heartWants = int(input("How many times do you love me"))
runThisLoop = 0
while runThisLoop < heartWants:
    print("I love this many times")
    runThisLoop = runThisLoop + 1

    #break allows for the code to end however not good practice

print("The loop end, and i am outside loop")
#when you see a statement that is repetitive and/or need to fill data
#and/or need to retrieve more than one data sets

#structure oof a for loop
# for variable  in list:
    #code here
    #run for loop until end
    #will run through a list from the beginning to end
#outside code here won't run until end of for loop
groceryList = ["Apple", "Banana", "Cherry", "Bread", "Eggs", "Cereal"]
for item in groceryList:
    print(item)
print("The end of the list, and out of the loop")


def outputFunctions(answer):
    print("The answer to your query is: ", answer)
continueLoop = True
calculation = 0
while continueLoop:
    var1 = int(input("Enter a number"))
    var2 = int(input("Enter another number"))
    if calculation == 0:
        answer = var1 * var2
    elif calculation == 1:
        answer = var1 / var2
    elif calculation == 2:
        answer = var1 // var2
    elif calculation == 3:
        answer = var1 % var2
    elif calculation == 4:
        answer = var1 + var2
    elif calculation == 5:
        answer = var1 - var2
        continueLoop = False

    outputFunction(answer)
    calculation = calculation + 1




