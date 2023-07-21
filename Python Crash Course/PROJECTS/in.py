# text = ["james", "binta"]
# x = text[0].index("a")
# print(x)

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
