class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):  # This is a method
		return f"{self.name} is {self.age}yrs old."

	def speak(self, sound):  # This is a method
		return f"{self.name} says {sound}."


my_dog = Dog("Blackie", 4)
print(my_dog.name)
my_dog.age = 5
print(my_dog.__str__())
print(my_dog.speak("woof"))
