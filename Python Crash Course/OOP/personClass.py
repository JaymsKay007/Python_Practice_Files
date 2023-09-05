"""This is a person class... PARENTS CLASS"""

"""Details about the person"""


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


"""Details about the person company... PARENTS CLASS"""


class Company:

	def company_data(self, company_name, company_location):
		self.company_name = company_name
		self.company_location = company_location


"""Employee ... CHILD CLASS"""


class Employee(Person, Company):
	def employee_data(self, salary, skills):
		print(f"My name is {self.name} and I'm {self.age}years old. I work at {self.company_name} and "
		      f"it's located in {self.company_location} State. My salary is {salary} and I'm "
		      f"providing them with my {skills} skills.")


james = Employee("James", 31)
# james.person_data()
james.company_data("Google", "California")
james.employee_data("$50,000", "Software developer")
