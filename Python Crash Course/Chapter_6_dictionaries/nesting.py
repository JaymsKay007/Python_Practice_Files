# A  dictionary in a list...

"""
alien0 = {"color": "green", "points": 5}
alien1 = {"color": "yellow", "points": 10}
alien2 = {"color": "red", "points": 15}

aliens = [alien0, alien1, alien2]

for alien in aliens:
    print(alien)
"""
# Create a list with 30 aliens.
# Make an empty list for storing aliens
aliens = []
# Make 30 gren aliens
for alien_number in range(30):
    new_aliens = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_aliens)
    # print(len(aliens))
# Show the first 5 aliens.
print("Show the first 5 aliens.")
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens is: {len(aliens)}")

# A list in a dictionary...
""" 
Rather than putting a dictionary inside a list, it’s sometimes useful to put
a list inside a dictionary. For example, consider how you might describe a
pizza that someone is ordering. If you were to use only a list, all you could
really store is a list of the pizza’s toppings. With a dictionary, a list of toppings
can be just one aspect of the pizza you’re describing.
In the following example, two kinds of information are stored for each
pizza: a type of crust and a list of toppings. The list of toppings is a value
associated with the key 'toppings'. To use the items in the list, we give the
name of the dictionary and the key 'toppings', as we would any value in the
dictionary. Instead of returning a single value, we get a list of toppings:
"""

# Store information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

# Summarize the order.
print(
    f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    if topping == "mushrooms":
        print("We're out of mushrooms.\nSo you'll get:")
    else:
        print(topping.title())
print("Thanks for ordering.")


favourite_language = {
    "james": ["python", "javascript"],
    "bayoh": ["javascript", ],
    "rashida": ["ruby", ],
    "mohamed": ["java", "C"],
    "joel": ["python", ],
}


for name, languages in favourite_language.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")



