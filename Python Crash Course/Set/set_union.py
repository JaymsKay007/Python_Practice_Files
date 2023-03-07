# A UNION and PIPE| takes all the data in a set{} and produce a new set{} without any duplicate
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# PIPE |
piping = a | b
print(piping)

# UNION
un = a.union(b)
print(un)

un1 = b.union(a)
print(un1)
