age = int(input("How old are you?: "))
vote = input("Did you register?").lower()

if age >= 18 and vote == "yes":
    print("You're old enough to vote.")
elif age >= 18 and vote == "no":
    print("You didn't register, so you can't vote.")
else:
    print("You can't vote because you're below 18yrs.")
