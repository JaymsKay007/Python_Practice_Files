"""
Removing All Instances of Specific Values from a List...
Say you have a list of pets with the value 'cat' repeated several times. To
remove all instances of that value, you can run a while loop until 'cat' is no
longer in the list.
"""

pets = ["cat", "dog", "rabbit", "goldfish", "cat", "dog", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
    print("There's no longer cat in the pets list.")
print(pets)
