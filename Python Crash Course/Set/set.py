"""
            SET {}
1. Unordered collection of items.
2. Every item it unique.
3. Every element must be immutable.
4. A set mutable.
5. Can be used to perform mathematical set operations.
"""
# INDEXING OR SLICING DOESN'T WORK IN SET()

names = {"james", "binta", "tina", "rashida", "mohamed"}
print(type(names))

my_set = {1, 2, 2, 3, 3, "hello", (7, 8, 7, 8, 9)}
print(my_set)
print(type(my_set))

my_set1 = set([2, 4, 6, 8])
print(my_set1)

# ADDING TO A SET{}
my_set1.add(10)
print(my_set1)

# UPDATE... ADD MULTIPLE ELEMENTS, IT CAN TAKE LIST, TUPLE, STRINGS N MUCH MORE
my_set1.update(["james", "joel", 2, 4])
print(my_set1)

# DELETING ON A SET{}
my_set1.discard("james")
print(my_set1)

my_set1.remove("joel")
print(my_set1)

my_set1.clear()
print(my_set1)

# del my_set1
# print(my_set1)
