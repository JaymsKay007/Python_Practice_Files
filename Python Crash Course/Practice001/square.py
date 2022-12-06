# squares = []
# for value in range(1, 11):
#     squares.append(value**2)
# print(squares)

# 2nd method
squares = [value**2 for value in range(1, 11)]
print(squares)

# List of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
minimum = min(digits)
maximum = max(digits)
addition = sum(digits)
print(f"The minimum number is {minimum}.")
print(f"The maximum number is {maximum}.")
print(f"The total for all the numbers is {addition}.")
