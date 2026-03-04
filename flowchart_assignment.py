harry = int(input("How much money does Harry have: "))
jude = int(input("How much money does Jude have: "))

if harry < 8:
    print("Harry cannot see the movie he has to go to the arcade.")
if harry >= 8:
    print("Harry can go to the movie. Enjoy!")

if jude < 8:
    print("Jude cannot see the movie she has to go to the arcade.")
if jude <= 8:
    print("Jude can go to the movie. Enjoy!")

if (harry >=8) and (jude >= 8):
    print("You can see the movie with your friend.")
if (harry >= 8)or (jude >= 8):
    print("Only one can see the movie.")
if (harry < 8)and (jude < 8):
    print("You have to go to the arcade with your friend.")
