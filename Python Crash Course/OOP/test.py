class Person:
	def __init__(self, name, age, wife):
		self.name = name
		self.age = age
		self.wife = wife

	def family(self):
		return f"Mr.{my_info.name} is {my_info.age}yrs old and he's married to Madam {my_info.wife} " \
		       f"and they've 3 children together."


my_info = Person("James", 31, "Binta")
print(my_info.name)
print(my_info.family())
