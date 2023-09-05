class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"My name is {self.name} and I'm {self.age}years old."

	def speak(self, sound):
		return f"{self.name}  loves saying {sound}"


class Poodle(Dog):
	def speak(self, sound="woo ooo"):
		return f"{self.name}  loves saying {sound}"


class Frug(Dog):
	def speak(self, sound="wof wof"):
		return f"{self.name}  loves saying {sound}"


class Dachshund(Dog):
	def speak(self, sound="haa haa"):
		return f"{self.name}  loves saying {sound}"


blackie = Poodle("Blackie", 9)
miko = Frug("Miko", 7)
max = Dachshund("Max", 5)

print(blackie.speak())
print(miko.speak())
print(max.speak("Grrre "))  # This overwrite the default sound

print(blackie, blackie.speak())
