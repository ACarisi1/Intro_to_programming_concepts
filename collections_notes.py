#create a lists in python
#lets start with a list of fruit

fruitList = ["Apple", "Orange", "Banana", "Cherry", "Grapes"]
print(fruitList)
#lists are muteable (can be changed)
#dynamic (can grow and shrink)

#specific item in a list
print(fruitList[1])

#update an index of a list
fruitList[2] = "Pear"
print(fruitList)

#add to a list
#can add duplicates
fruitList[2] = "Orange"
fruitList.append("Pear")
print(fruitList)

#insert in a given spot in a list
fruitList.insert(2, "Grape Fruit")
print(fruitList)

#remove from a list
#will remove one duplicate from the list, however will remove first one it finds
fruitList.pop(2)
print(fruitList)

fruitList.remove("Pear")
print(fruitList)

#returns length of the list
countfruitList = len(fruitList)
print(countfruitList)

#tuples are static (cannot grow or shrink)
