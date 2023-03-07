# COUNT METHOD... THIS COUNT HOW MANY TIMES A NUMBER APPEARS IN THE TUPLE
my_tuple = (1, 1, 1, 1, 2, 2, 3, 4, 2, 4, 5, 1, 2, 3)
print(my_tuple.count(2))

# INDEX...
# index_tuple = my_tuple.index(3)
index_tuple = my_tuple.index(3, 7)  # This locate the index of 3 after index 7 in the tuple.
print(index_tuple)

check = 5 in my_tuple
check2 = 8 in my_tuple
check3 = 7 not in my_tuple
print(check)
print(check2)
print(check3)
