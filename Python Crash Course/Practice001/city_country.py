"""
City Names: Write a function called city_country() that takes in the name
of a city and its country.
"""


# city1 = input("Which City are you from?: ")
# country1 = input("Which Country are you from?: ")


def city_country(city, country):
    answer = f"{city}, {country}."
    return answer.title()


responses = {}  # Create an empty dictionary
while True:
    print("\n(Enter 'q' at anytime to quit)")

    city1 = input("Which City are you from?: ")
    if city1 == "q":
        break
    country1 = input("Which Country are you from?: ")
    if country1 == "q":
        break
    nationality = city_country(city1, country1)

    # The empty responses take data from the users and store it.
    responses[city1] = country1
# Create an FOR LOOP to print out the input from the dictionary(responses)
for cities, countries in responses.items():
    print(f"{cities.title()}, {countries.title()}")
