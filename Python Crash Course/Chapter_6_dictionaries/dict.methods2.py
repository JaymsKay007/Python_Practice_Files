my_dict = {"apples": 0.49, "banana": 0.69, "pear": 0.99, "bread": 2.5}
print(my_dict)

# This put the items into peers
dict_items = my_dict.items()
print(dict_items)

# This let u access the keys in a dictionary and return the in a list.
key = my_dict.keys()
print(key)

# This let u access the value in a dictionary and return  in a list.
val = my_dict.values()
print(val)

# for key in my_dict.keys():
print("These are the prices of the items:")
for key, value in my_dict.items():
    print(key.title(), "=", "$", value)

# This sort out the list in alphabetical order
print(sorted(my_dict))
