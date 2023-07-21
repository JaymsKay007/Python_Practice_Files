class Dog:
	"""User-defined object to represent and manage dog."""

	def __init__(self, name, age):
		self.name = name
		self.age = age


my_dog = Dog("Pete", 5)

print(my_dog.name)
print(my_dog.age)

# My own way of modifying class:
# class Dog:
# 	"""User-defined object to represent and manage dog."""
#
# 	def __init__(self, name, age):
# 		self.name = input("What's the name of your dog?: ")
# 		self.age = input("how old is your dog?: ")
#
#
# my_dog = Dog("", 0)
#
# print(my_dog.name)
# print(my_dog.age)
