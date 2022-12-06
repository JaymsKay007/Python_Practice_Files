# Nested IF/ELSE Block

print("Welcome to Rollercoaster")
height = int(input("What's your height in cm? "))

if height >= 120:
    print("You can ride the Rollercoaster.")
    age = int(input("What's your age?: "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You can't ride the Rollercoaster, bcos you're too short.")
