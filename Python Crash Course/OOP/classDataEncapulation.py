""""
There are 3 types of data encapsulation in python class.
PUBLIC ENCAPSULATION = This kind of encapsulation is accessable from anywhere, in and outside the class.
PRIVATE ENCAPSULATION = This kind of encapsulation is accessable only within the class. E.g.
self.__name = name
PROTECTED ENCAPSULATION = This kind of encapsulation is accessable only within the parent class and it sub-classes. E.g.
self._name = name
"""


# PUBLIC ENCAPSULATION
class Employee:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def description(self):
		print(f"My name is {self.name} and i'm {self.age}yrs old.")


james = Employee("James", 31)
james.description()
print(f"THIS IS A PUBLIC CLASS, I CAN ACCESS THE OBJECTS OUTSIDE THE CLASS...  His name is {james.name} "
      f"and "
      f"he's {james.age}yrs old. ")


# PRIVATE ENCAPSULATION
class Employee:
	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	def description(self):
		print(f"THIS IS A PRIVATE CLASS. I CAN ONLY ACCESS THE OBJECT WITHIN THE CLASS... My name is"
		      f" {self.__name} and I'm"
		      f" {self.__age}yrs old.")


james = Employee("James", 31)
james.description()
# print(f"His name is {james.name} and he's {james.__age}yrs old. ") #THIS PRINT STATEMENT CANT ACCESS
# THE CLASS BCOS IT'S PRIVATE.
