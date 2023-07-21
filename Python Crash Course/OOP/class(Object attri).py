class Dog:
	"""User-defined object to represent and manage dog."""

	kingdom = "Animal"  # This is used as default attribute for all the  object in this class(DOG) and

	# it's used outside the __init__function.

	def __init__(self, name, age):
		self.name = name
		self.age = age


my_dog = Dog("Max", 5)

print(my_dog.kingdom)
print(my_dog.name)
print(my_dog.age)
