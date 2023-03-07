my_dict = {"apples": 0.49, "banana": 0.69, "bread": 2.5, "pear": 0.99}
print(my_dict)

# This methods delete items from the dictionary
pop_off = my_dict.pop("apples")  # This deletes apple from the dictionary
# print(pop_off)
print(my_dict)

# This adds items to the dictionary
my_dict["orange"] = 2.60
print(my_dict)

# This deletes the last items in the dictionary
my_dict.popitem()
print(my_dict)

# This clears everything in the dictionary and leaves it empty
my_dict.clear()
print(my_dict)

# This deletes the entire dictionary
del my_dict
print(my_dict)
