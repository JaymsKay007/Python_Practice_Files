"""
def make_pizza(size, *toppings):
    print(f"Making a {size} pizza with the following toppings: ")
    for topping in toppings:
        print(topping.title())

# make_pizza("small", "mashroom", "pepperoni", "beef")
"""

size_quest = input("Which pizza do u want?: ").strip()
topping_quest = input("Which toppings do u want on your pizza?: ").strip()


def make_pizza(size=size_quest, *toppings):
    print(f"Making a {size.strip()} pizza with the following toppings: ")

    for topping in toppings:
        print(topping.strip().title())


make_pizza(size_quest, topping_quest)
