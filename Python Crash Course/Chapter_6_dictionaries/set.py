favourite_language = {
    "james": "python",
    "bayoh": "javascript",
    "rashida": "ruby",
    "mohamed": "java",
    "joel": "python",
}

"""
set(): A set is a collection in which each item must be unique:::
It's also a method to get rid of duplicate names in a list or dictionary.
    When you wrap set() around a list that contains duplicate items, Python
identifies the unique items in the list and builds a set from those items.
"""
print("\nThe following language have been mentioned:")
for language in set(favourite_language.values()):
    print(language.title())
