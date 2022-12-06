import random

your_name = input("What's your name?")
their_name = input("What's your spouse name?")

love_score = random.randint(1, 100)

if love_score <= 49:
    print(f"{your_name} and {their_name} love score is {love_score}% and they're not compatible.")
elif love_score <= 70:
    print(f"{your_name} and {their_name} love score is {love_score}% and they're compatible.")
else:
    print(f"{your_name} and {their_name} love score is {love_score}% and they're really experiencing true love.")
