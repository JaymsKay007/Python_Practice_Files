class Dog:
	"""User-defined object to represent and manage dog."""

	def __init__(self, name, age):
		self.name = name
		self.age = age


my_bruno = Dog("Bruno", 5)

print(my_bruno.name)
print(my_bruno.age)
# Another instance of different Bruno with the same info
your_bruno = Dog("Bruno", 5)

print(your_bruno.name)
print(your_bruno.age)
"""
This info show that even both dogs has the same info, they'll save differently on the class with 
different memory allocation.
 """
print(my_bruno)
print(your_bruno)

# This shows they're 2 different dogs in the class/
if my_bruno == your_bruno:
	print(True)
else:
	print(False)
