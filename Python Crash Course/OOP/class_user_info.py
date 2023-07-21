class UserInfo:
	def __init__(self, name, age, job):
		self.name = input("What's your name?: ")
		self.age = int(input("What's your age?: "))
		self.job = input("What's your job?: ")

	#
	def description(self):
		print(
			f"Mr. {my_info.name} is {my_info.age}yrs old and his current job is a {my_info.job} at Google Company")


my_info = UserInfo("", 0, "")
print(my_info.name)
print(my_info.age)
print(my_info.job)
print(my_info.description())
# print(
# 	f"Mr. {my_info.name} is {my_info.age}yrs old and his current job is a {my_info.job} at Google Company")
