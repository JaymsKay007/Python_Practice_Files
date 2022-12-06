# This program ask the user what type of car they want to rent and them they'll find info about the car.
car = input("What type of Car do you want to rent? ")

if car == " ":
    print("Please input a car name.")
else:
    print(f"Let me see if I can find you a {car}.")
