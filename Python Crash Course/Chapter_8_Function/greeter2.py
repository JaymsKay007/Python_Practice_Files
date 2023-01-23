def get_fullname(firstname, lastname):
    fullname = f"{firstname} {lastname}."
    return fullname.title()


while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at anytime to quit)")
    fname = input("Firstname: ")
    if fname == "q":
        break
    lname = input("Lastname: ")
    if lname == "q":
        break
    formatted_name = get_fullname(fname, lname)
    print(f"\nHello {formatted_name}")
