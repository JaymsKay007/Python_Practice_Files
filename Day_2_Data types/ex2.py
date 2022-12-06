# Create a program using maths and f-strings that tells us how many days, weeks, and
# months left if we live until 90yrs old.

# It'll take your current age as thr input and output a message with out time left in this format.
# eg. You've x days, y weeks and z months left to live.

age = input("How old are you?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You've {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left to live."
print(message)
