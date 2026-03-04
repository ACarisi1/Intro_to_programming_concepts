book = {
    "title": "A SOng of Ice and FIre",
    "author": "George R.R. Martin",
    "year": 1996
}

print(book)
print(book["year"])

myTitle = book["title"]
myTitle = book.get("title") #line 10 and 11 preform the same task
print(myTitle)

print (book.keys())
print(book.values())

book["pages"] = 254 #dictionaries are dynamic
print(book)

book["year"] = 1984
book.update({"year":1997})
print(book)

if "author" in book:
    print("Yes it is in the dictionary")

book.pop("year")
print(book)

book.popitem()
print(book)

#del book
#print(book) #will delete entire dictionary

#book.clear()
#print(book) #will clear out the dictionary but will not delete

students = {
    "vid1111": {
        "name": "George",
        "gpa": 1.5
    },
    "vid1232":{
        "name": "Jenny",
        "gpa": 2.0
    },
    "vid3863":{
        "name": "Samantha",
        "gpa": 3.7
    }
}

print(students["vid1111"]["name"], students["vid1111"]["gpa"])
print(students["vid1232"]["name"])
print(students["vid3863"]["name"])




