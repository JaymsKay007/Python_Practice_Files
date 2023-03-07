# Two times table...
# def two_times(*num):
#     num = int(input(f"Input any number multiply by 2 and you'll get the result:\n"
#                     "Which number you want to multiply by 2? "))
#     print("The answer is: ", num * 2)
#
#
# two_times(0)


def sandwich(*items):
    print("You order sandwich with: ")
    for index, item in enumerate(items):
        print(index + 1, item)

    print(f"You sandwich includes {len(items)} items.")


# sandwich("bread", "cheese", "egg", "mayonnaise")
# sandwich("onion", "butter", )


# importing multiple function from a module
from function_module import pizza, two_times

pizza.make_pizza(pizza.size_quest, pizza.topping_quest)
