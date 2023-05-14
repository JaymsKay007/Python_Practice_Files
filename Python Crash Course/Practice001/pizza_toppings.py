"""
Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""


prompt = (
    "Welcome to James Fast Food."
    + "\nEnter the toppings you want on your pizza: "
)
while True:
    toppings = input(prompt)
    if toppings == "quit":
        break
    else:
        print(f"I’ll add that {toppings} to your pizza.\n")
