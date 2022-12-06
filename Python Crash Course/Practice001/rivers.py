"""
Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    "rokel": "sierra leone",
    "victoria falls": "kenya",
    "nile": "egypt",
}

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

# • Use a loop to print the name of each river included in the dictionary.
for river in rivers.keys():
    print(river.title())

# • Use a loop to print the name of each country included in the dictionary.
for country in rivers.values():
    print(country.title())
