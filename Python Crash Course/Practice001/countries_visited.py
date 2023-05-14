"""
Instructions
You are going to write a program that adds to a travel_log.
You can see a travel_log which is a List that contains 2 Dictionaries.
Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.
You've been to Moscow and Saint Petersburg.
DO NOT modify the travel_log directly. You need to create a function that modifies it.

...Hint...
Look at the function call above to see what the name of the function should be.
The inputs for the function are positional arguments. The order is very important.
Feel free to choose your own parameter names.
"""
travel_log = [
    {
        "countries": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "countries": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(countries_visited, times_visited, cities_visited):
    new_country = {
        "countries": countries_visited,
        "visits": times_visited,
        "cities": cities_visited,
    }
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

"""
# THIS OTHER CODE TAKES DATA FROM THE USERS AND ADD IT TO THE TRAVEL LOG LIST...


travel_log = [
    {
        "countries": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "countries": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# TAKES DATA FROM THE USER...
contri = input("Which new country have you visited?: ")
waka_tem = int(input("How many times have you visited the country?: "))
city_pass = input("How many cities have you visited in the country?: ")


def add_new_country(countries_visited=contri, times_visited=waka_tem, cities_visited=city_pass):
    new_country = {}
    new_country["countries"] = countries_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country(contri, waka_tem, [city_pass])
print(travel_log)

"""
