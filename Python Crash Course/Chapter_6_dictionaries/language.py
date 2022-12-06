# sorted()
# set()

favourite_language = {
    "james": "python",
    "bayoh": "javascript",
    "rashida": "ruby",
    "mohamed": "java",
    "joel": "python",
}

friends = ["bayoh", "tina", "rashida"]

for name in favourite_language:
    print(f"Hi {name.title()}")

    if name in friends:
        language = favourite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

# This let us findout if a person is not in our dictionary (favourite_language).
if "Erin" not in favourite_language:
    print("Erin, please take our poll.\n")

 
