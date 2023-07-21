# This change the name of the attributes...
class Dog:
	def __init__(self, name, age, owner):
		self.name = name
		self.age = age
		self.owner = owner

	def description(self):
		return f"Mr. {my_dog.owner} dog  name is '{my_dog.name}' and he's {my_dog.age}yrs old."


my_dog = Dog("Max", 3, "James")
my_dog.name = "Bingo"
my_dog.owner = "Bernard"
print(my_dog.name)
print(my_dog.age)
print(my_dog.owner)
print(my_dog.description())
