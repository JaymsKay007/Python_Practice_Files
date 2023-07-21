# PARENT OR BASE CLASS

class Profession:
	kingdom = "Human"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"Mr. {self.name} is {self.age}yrs old, and his current job is {self.work()} " \
		       f"and he's " \
		       f" {self.kingdom.upper()}."


# def work(self, job):
# 	return f"Mr.{self.name} is a {job}"


# PARENT OR BASE CLASS
class SoftwareDeveloper(Profession):
	def work(self, job="Software Developer"):
		return f" {job}"


class Teacher(Profession):
	def work(self, job="Teacher"):
		return f" {job}"


class Pilot(Profession):
	def work(self, job="Pilot"):
		return f" {job}"


class Soldier(Profession):
	def work(self, job="Soldier"):
		return f" {job}"


james = SoftwareDeveloper("James", 31)
jack = Teacher("Jack", 30)
joe = Pilot("Joe", 43)
johnson = Soldier("Johnson", 29)

print(james.work())
print(james)
print(jack)
print(johnson)
