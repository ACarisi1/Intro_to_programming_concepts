print(""
      "Here is the Plane seating chart\n"
      "1:    +      + \n"
      "2:    X      + \n"
      "3:    +      X \n"
      "4:    X      X \n"
      "5:    X      + \n"
      "6:    +      + \n"
      "7:    +      X \n"
      "8:    X      + \n"
      "9:    X      + \n"
      "10:   +      X \n"
      "First row is first class\n"
      "Rows  4 and 7 are exit rows\n"
      "Seats marked with an X are taken\n")
def available_seats():
      print("Your have selected", plane_selection)
      available.remove(plane_selection)
      taken.append(plane_selection)
      seat_selections.append(plane_selection)
def taken_seats():
      print("You have selected a taken seat\n"
            "Please review the seating chart\n"
            "And make another selection")
def firstClass_seats():
      class_selection = input("Your chose a First Class ticket which cost $150 extra\n"
                              "Do you still want this selection? ").upper()
      if class_selection == "YES":
            print("Great! You will enjoy the finest service and dining")
            first_class.remove(plane_selection)
            taken.append(plane_selection)
            seat_selections.append(plane_selection)
      else:
            return input("Choose another seat").upper()
def exit_seats():
      safety_question = input("You have selected an exit row\n"
                              "Are you able to help in an emergency?").upper()
      if safety_question == "YES":
            print("Thank you for your help\n"
                  "The flight attendant will provide more information\n"
                  "when you take your seat.")
            exit_rows.remove(plane_selection)
            taken.append(plane_selection)
            seat_selections.append(plane_selection)
      else:
            return input("Choose another seat").upper()
def done():
      print("Here are your selections", seat_selections)
      print("Enjoy your flight\n"
            "See Ya Real Soon")

available = ["2B","3A","5B","6A","6B","8B","9B","10A"]
taken = ["2A","3B","5A","7B","8A","9A","10B"]
first_class = ["1A","1B",]
exit_rows = ["7A"]
seat_selections = []

plane_selection = input("Please enter your selection: \n"
                        "Enter done to head to checkout\n").upper()
while plane_selection != "DONE":
      if plane_selection in available:
            available_seats()
      elif plane_selection in taken:
            taken_seats()
      elif plane_selection in first_class:
            new_choice = firstClass_seats()
            if new_choice:
                  plane_selection = new_choice
                  continue
      elif plane_selection in exit_rows:
            new_choice = exit_seats()
            if new_choice:
                  plane_selection = new_choice
                  continue
      else:
            print("Please enter a valid selection")
      plane_selection = input("Please enter your selection: \n"
                              "Enter done to head to checkout\n").upper()
done()


