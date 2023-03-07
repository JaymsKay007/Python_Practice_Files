evens = []
# for x in range(31):
#     if x % 2 == 0:
#         evens.append(x)
# print(evens)

# OR
for x in range(11):
    evens.append(x * 2)
print(evens)

# OR LIST COMPREHENSION
evens1 = [(x * 2) for x in range(11)]
print(evens1)

# Create a list of even numbers from 0 to 20 excluding numbers divisible by 6, using list comprehension...
evens2 = [(x * 2) for x in range(11) if x * 2 % 6 != 0]
print(evens2)
