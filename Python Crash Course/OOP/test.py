class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age}yrs old."

	def speak(self, sound):
		return f"{self.name} says {sound}"


class ShihTzu(Dog):
	def speak(self, sound="Shih woof"):
		return f"{self.name} says {sound}"


class Dachshund(Dog):
	def speak(self, sound="woof"):
		return f"{self.name} says {sound}"


class Poodle(Dog):
	def speak(self, sound="woo woo"):
		return f"{self.name} says {sound}"


class Frug(Dog):
	def speak(self, sound="fruuu"):
		return f"{self.name} says {sound}"


dolly = ShihTzu("Dolly", 7)
flo = Dachshund("Dolly", 9)
sassy = Poodle("Sassy", 3)
betty = Frug("Betty", 1)

print(dolly.speak())
print(flo.speak())
