print("Welcome to Rollercoaster")
height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the Rollercoaster.")

    age = int(input("What's your age?: "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7.")
    else:
        bill = 12
        print("Adult ticket are $12.")

    photo = input("Do you want a photo taken? Y or N. ")

    if photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You can't ride the Rollercoaster, bcos you're too short.")
