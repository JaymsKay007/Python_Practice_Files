# This function produce a full name of a person

def get_formatted_name1(first_name, last_name, ):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


name1 = get_formatted_name1("james", "konomanyi")
print(name1)

# Function with Middle name...
"""
To make the middle name optional, we can give the middle_name argument
an empty default value and ignore the argument unless the user provides a
value. To make get_formatted_name() work without a middle name, we set the
default value of middle_name to an empty string and move it to the end of the
list of parameters:
"""
fname = input("What's your firstname?: ")
mname = input("What's your middlename?(Optional): ")
lname = input("What's your lastname?: ")


def get_full_name(first_name=fname, last_name=lname, middle_name=""):
    if middle_name:
        full_name = f"Hello {first_name} {middle_name} {last_name}."
    else:
        full_name = f"Hello {first_name} {last_name}."
    return full_name.title()


name = get_full_name(fname, lname, mname)
print(name)
