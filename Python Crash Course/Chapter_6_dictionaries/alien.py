
alien_0 = {"color": "green",
           "point": 5}

# print(alien_0)

print(alien_0["color"])
print(alien_0["point"])

# Adding a key/value to an existing DICTIONARY
alien_0["x_position"] = 0
alien_0["y_position"] = 25
alien_0["speed"] = "fast"

print("This is the Alien attributes:", alien_0)

"""
For a more interesting example, let’s track the position of an alien that
can move at different speeds. We’ll store a value representing the alien’s
current speed and then use it to determine how far to the right the alien
should move:

1. Move the alien to the right.
2. Determine to move the alien based on its current speed.
"""
if alien_0["speed"] == "slow":
    alien_0["x_position"] = 1
elif alien_0["speed"] == "medium":
    alien_0["x_position"] = 2
else:
    alien_0["x_position"] = 3
    print("This must be a fast Alien.")
print(f"New position: {alien_0['x_position']}")

# Removing a key/value pair from a dictionary.
del alien_0["speed"]
print("This is the Alien attributes:", alien_0)
# adding key value to an empty dictionary
"""
James_info = {}

James_info["Name"] = "James"
James_info["Age"] = 30
James_info["Location"] = "Belia Park"
James_info["PhoneNo"] = 23278265881

# print(James_info)
James_info["Name"] = "Bernard"
James_info["Job"] = "Computer programmer"
# print(James_info)
print(
    f"This is the information of Mr {James_info['Name']}, he's {James_info['Age']}yrs old,\
 lives at {James_info['Location']} and he\'s a {James_info['Job']}\
 and you can contact him on {James_info['PhoneNo']}.")
"""
