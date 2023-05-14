# print(shopping_list[-1])

position = [1, 2, 3, 4, 5, [6, 7, 8, 9]]
print(position[5][2])  # Find the position of 8
print(position[-1][-2])  # Find the position of 8

shopping_list = [
    "Apples",
    "Orange",
    "Mango",
    "Pine Apples",
    "Lemon",
    "Gravy",
    "Soup",
    "Chicken",
    "Bread",
]
print(shopping_list)
# SLICING LIST
print(shopping_list[2:-3])
print(shopping_list[3:6])

# LIST METHOD
names = ["James", "Binta", "Rashida", ]
names.reverse()  # reverse the list order
names.append("Jack")
names.copy()
print(names)

# SORTING LIST
number = [1, 2, 3, 4, 5]
number.sort(reverse=True)
print(number)

# MODIFYING A LIST
shopping_list[:3] = ["Phone", "Charger", "Sim", ]
print(shopping_list)

# REMOVING ELEMENT FROM A LIST
shopping_list.pop()  # This deletes the last item on the list
shopping_list.pop(3)  # This deletes the item at position 3 on the list
# del shopping_list #This deletes the whole list
# del shopping_list[1] #This deletes the item at position 1
del shopping_list[1:3]  # This deletes the item at position 1 and 3
shopping_list.remove("Phone")  # This removes specific item on the list
shopping_list.clear()  # This will clear all the elements in the list 
print(shopping_list)
