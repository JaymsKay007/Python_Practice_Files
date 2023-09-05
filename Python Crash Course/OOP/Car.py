# THE CAR CLASS
class Car:
	"""A simple attempt to represent a car"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing a car milage"""
		print(f"This car has {self.odometer} miles on it.")

	def update_odometer(self, milage):
		"""This update the car odometer and prevent the odometer from rolling back"""
		if milage >= self.odometer:
			self.odometer += milage
		else:
			print("You can't roll back an odometer")

	def fill_gas_tank(self):
		print("50 litres of gas fills this car tank.")


# new_car = Car("audi", "a4", 2023)
# print(new_car.get_descriptive_name())
#
# new_car.read_odometer()  # This is the original odometer with zero miles
# new_car.update_odometer(70)  # This update the car milage to 600 miles
# new_car.read_odometer()

# THE BATTERY CLASS
class Battery:
	def __init__(self, battery_size=40):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")

	def upgrade_battery(self):
		# This method upgrades the battery
		self.battery_size = 70
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides"""
		if self.battery_size == 40:
			range = 150
		elif self.battery_size == 70:
			range = 250

		print(f"This car can go about {range} miles on full charge.")


# ELECTRIC CAR CHILD CLASS
class ElectricCar(Car):
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class.
			Then initializing attributes specific to an electric car"""

		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		print("This car doesn't use gas.")


tesla = ElectricCar("tesla", "S20", 2024)
# print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.fill_gas_tank()
tesla.battery.upgrade_battery()
tesla.battery.get_range()
