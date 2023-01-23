# RETURNING A DICTIONARY...
# Returning a dictionary of information about a person... And adding other key details about the person through the
# function
fname = input("What's your firstname?: ")
lname = input("What's your lastname?: ")
age1 = int(input("How old are you?: "))
location1 = input("Which country are you from?: ")


def build_person(first_name=fname, last_name=lname, age=age1, location=location1):
    person = {"first": first_name,
              "last": last_name, }
    if age:
        person["age"] = age
    if location:
        person["location"] = location
    return person


# name = build_person("james".title(), "ellie".title(), age=30, location="Sierra Leone ")
name = build_person(fname, lname, age1, location1)
print(name)
