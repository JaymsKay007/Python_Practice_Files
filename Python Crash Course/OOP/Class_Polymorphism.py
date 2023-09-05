""" Polymorphism is a object of Object-Oriented Programming. I enbles using a single interface with the
 input of a different data types, different classes or maybe for a different number of inputs."""


class Dog:
	def __init__(self, owner, color, name):
		self.owner = owner
		self.color = color
		self.name = name

	def description(self):
		print(f"{self.owner} owns a dog name {self.name} with a {self.color} color.")

	def toys(self):
		print(f"{self.owner} dog favourite toy is a rubber bone.")


class Cat:
	def __init__(self, owner, color, name):
		self.owner = owner
		self.color = color
		self.name = name

	def description(self):
		print(f"{self.owner} owns a cat name {self.name} with a {self.color} color.")

	def toys(self):
		print(f"{self.owner} cat favourite toy is a rubber rat.")


dog1 = Dog("James", "Black", "Max")
cat1 = Cat("Binta", "Gray", "Felix")

for animal in (dog1, cat1):
	animal.description()
	animal.toys()
