"""
T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


# Example 1
def make_shirt(size, message):
    print(f"Dear valued customer, you choose '{size}' shirt with the message,'{message}'.")


make_shirt("Extra large", "Happy birthday dear")  # Positional arguments
make_shirt(size="Extra large", message="Happy birthday dear")  # keyword arguments

# 2nd example
"""Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""

shirt_choice = input("What's your shirt size? ")


def shirt(size="large", message="I love Python"):
    if shirt_choice == "small" or "extra small":
        print(f"Dear valued customer, you choose '{shirt_choice}' shirt with the message 'Hello little one'.")


shirt("small")

# example 3
"""
Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""
country1 = input("Which country are you from: ")


# city1 = input("Which city are you from: ")


def describe_city(city, country=country1):
    print(f"{city.title()} is in {country.title()}. ")


describe_city("freetown", country=country1)
