# The data in a tuple are immutable... They can be changed.
names = ("James", 300, "Tina",)
print(type(names))
print(names[0])
names[0]
print(names)
# Tuple can also be created without the parenthesis ()
my_tuple = "james", 23, [2, 3], True, 3.8,
print(my_tuple)
print(type(my_tuple))

my_tuple1 = "Tina",
print(type(my_tuple1))

# ACCESSING TUPLE()
my_tuple2 = (1, 2, 3, 4, 5, [6, 7, 8], (9, 10, 11))
# access_tu = my_tuple2[5][-1]
# access_tu = my_tuple2[-1][-3]
access_tu = my_tuple2[5:]
print(access_tu)
