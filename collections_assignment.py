def grade():
    average = sum(gradeList)/len(gradeList)
    print(average)
def gradeLetter():
    average2 = sum(gradeList)/len(gradeList)
    if average2 >= 90:
        print("A")
    elif average2 >= 80:
        print("B")
    elif average2 >= 70:
        print("C")
    elif average2 >= 60:
        print("D")
    else:
        print("F")
    print(average2)
inputGrades = int(input("Enter the students Grade: "))
gradeList = []
gradeList.append(inputGrades)
inputGrades = int(input("Enter the students next Grade: "))
gradeList.append(inputGrades)
inputGrades = int(input("Enter the students next Grade: "))
gradeList.append(inputGrades)
inputGrades = int(input("Enter the students next Grade: "))
gradeList.append(inputGrades)
inputGrades = int(input("Enter the students next Grade: "))
gradeList.append(inputGrades)


grade()
gradeLetter()


