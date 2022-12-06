favourite_language = {
    "james": "python",
    "bayoh": "javascript",
    "rashida": "ruby",
    "mohamed": "java",
    "joel": "python",
}

"""
    Looping Through a Dictionary’s Keys in a Particular Order __ sorted()::
Starting in Python 3.7, looping through a dictionary returns the items in
the same order they were inserted. Sometimes, though, you’ll want to loop
through a dictionary in a different order.
One way to do this is to sort the keys as they’re returned in the for loop.
You can use the sorted() function to get a copy of the keys in order:
"""
for name in sorted(favourite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


