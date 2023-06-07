import random

code = ["030", "033", "077", "080", "088", "090", "099"]
numbers = random.randint(123456, 999999)
code_choice = random.choice(code)
print(f"The winning number for this draw is {code_choice} {numbers}.")
