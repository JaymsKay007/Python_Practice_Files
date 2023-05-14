user0 = {
    "username": "jaymskay",
    "first": "james",
    "last": "kay",
}

# for _ in user0:
#     print(f"\nKey: {_},\nValue:", user0[_])

# This loop tru the Key, Value in a dictionary
# for key, value in user0.items():
#     print(f"\nKey:", {key})
#     print(f"Value:", {value})

# This loop tru the key in a dictionary
print("These are the Keys in the dictionary.")
for name in user0:
    print(name.title())

# This loop tru the value in a dictionary
print("These are the Value in the dictionary:")
for name in user0.values():
    print(name.title())
