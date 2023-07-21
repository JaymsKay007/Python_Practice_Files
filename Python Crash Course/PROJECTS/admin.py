user_names = ["James", "tina", "admin", "Rashida", "Med"]
for names in user_names:
    if names.title() == "Admin":
        print("Hello Admin, would you like to see a status report?.")
    else:
        print(f"Hello {names.title()}, thank you for logging in again.")

# users = []
# if users:
#     for user in users:
#         print(f"Hello {user.title()}, thank you for logging in again.")
# else:
#     print("The list is empty, we need to find some users.")
