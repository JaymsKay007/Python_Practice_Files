# LENGTH OF A  NUMBER
fav_numbers = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(len(fav_numbers))
print(len(fav_numbers[0]))
# RANGE
print(list(range(1, 11)))
print(list(range(0, 101, 10)))

# ZIP METHOD = This allow us to take 2 list and make a list with a tuple()..
names = ["James", "Binta", "Rashida", "Jamestina", "Mohamed"]
ages = [30, 30, 3, 12, 1]
names_and_ages = zip(names, ages)
print(names_and_ages)
names_ages_list = list(names_and_ages)
print(names_ages_list)

# INDEX METHOD
fav_num = [1, 2, 3, 4, 5, 6, 7, 8]
print(fav_num.index(3))

# COUNT = This let u know how many times a number is repeated in the code...
fav_numB = [1, 1, 1, 2, 3, 4, 4, 6, 5, 5, 6, 7, 9, 7, 8]
print(fav_numB.count(5))

# LIST MEMBERSHIP
fav_artists = ["James", "Wayne", "Joe", "Med"]
find_out = "James" not in fav_artists
find_out1 = "Joe" in fav_artists
find_out2 = "beyonce" in fav_artists
print(find_out, find_out1)
print(find_out2)

# SPLIT() AND JOIN() METHOD
# SPLIT() CHANGES STRINGS TO LIST
colours = "red, blue, green"
COLOUR_li = list(colours)
print(COLOUR_li)

colour_list = colours.split(",")
print(colour_list)

# a, b, c = colour_list  # colour_list This assign the colours to a variable of a,b,c
# print(c)
# print(b)

sentence = "I am a random sentence because I love learning Python"
sen = sentence.split(" ")
print(sen)

# This split the names below...
names = "James Binta Rashida Mohamed Jamestina Joel"
names_split = names.split(" ")
print(names_split)
for name in names_split:
    print(name)

# JOIN() Method
join_sentence = " ".join(sen)
print(join_sentence)

names_join = " Konomanyi, ".join(names_split)
print(names_join)

join_colours = " and ".join(colour_list)
print(join_colours)
