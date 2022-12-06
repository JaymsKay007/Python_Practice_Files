"""favorite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
language = favorite_language["edward"].title()
# for name in favorite_language:
print(f"Edward favorite programming language is {language}.")"""

# create a real life dictionary.
glossary = {
    "james": " likes coding in python.",
    "binta": " likes coding in javascript.",
    "rashida": " likes coding in C.",
    "mohamed": " likes coding in ruby.",
}
# for _ in glossary:
#     print(f"{_.title()}:\n", glossary[_])

for name, language in glossary.items():
    print(f"{name.title()}'s: {language.title()}")
