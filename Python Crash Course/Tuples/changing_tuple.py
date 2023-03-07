my_tuple = (1, 2, 3, 4, 5, [6, 7, 8], (9, 10, 11))
chng = my_tuple[5][2] = 80  # This is able to change bcos of the LIST inside the TUPLE
print(chng)
print(type(my_tuple[5]))
my_tuple[5].append(100)
print(my_tuple)
# CHANGING THE TUPLE
my_tuple = ("one", "two", "three")
add_tuple = my_tuple + ("four", "five", "six")
print(add_tuple)
print(my_tuple)

multiply_tuple = add_tuple * 2
print(multiply_tuple)

# DELETING A TUPLE
del multiply_tuple
