# DICTIONARY COMPREHENSION
squares = {x: x * x for x in range(6)}
print(squares)

# OR
squares = {x: x * x for x in range(6)}
print(squares)

# STORE ONLY EVEN NUMBERS IN THE DICTIONARY
even_squares = {x: x * x for x in range(11) if x % 2 == 0}
print(even_squares)
