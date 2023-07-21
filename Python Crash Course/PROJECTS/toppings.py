# requested_toppings =


# requested_toppings = ["mushrooms", "extra cheese", "pepperoni", "Green peppers"]

'''if "mushrooms" in requested_toppings:
    print("Adding mushrooms")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese")
if "pepperoni" in requested_toppings:
    print("Adding Pepperoni")
    
print("\n Finished making your pizza.")'''

# Checking for Special Items
''' 
for requested_topping in requested_toppings:
    if requested_topping == "Green peppers":
        print("Sorry, we're out of Green peppers.")
    else:
        print(f"Adding {requested_topping}")
print(("\n Finished making your pizza?.")
'''

# Checking That a List Is Not Empty
"""requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
else:
    print("Are you sure you want a plain pizza:")"""

# Using Multiple Lists
"""
People will ask for just about anything, especially when it comes to pizza
toppings. What if a customer actually wants french fries on their pizza? You
can use lists and if statements to make sure your input makes sense before
you act on it.
Let’s watch out for unusual topping requests before we build a pizza.
The following example defines two lists. The first is a list of available toppings
at the pizzeria, and the second is the list of toppings that the user has
requested. This time, each item in requested_toppings is checked against the
list of available toppings before it’s added to the pizza: 
"""

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print(f"\nFinished making pizza.")
