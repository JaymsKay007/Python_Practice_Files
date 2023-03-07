"""
ARGS
Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time.
"""


def sandwich_order(*items):
    print("You order sandwich with: ")
    for index, item in enumerate(items):
        print(index + 1, item)
    print(f"You order sandwich with {len(items)} items. ")


sandwich_order("Bread", "Lettuce", "Tomato", "Cheese", "Onion", )
print("\n")
sandwich_order("Bread", "Tuna", "Pickles", "Mustard")
