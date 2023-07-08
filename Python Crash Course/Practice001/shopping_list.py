""""
									THE SHOPPING LIST APP...
A Supermarket chain, a foodie, has asked you to create a Shopping list application to help their
customers whilst shopping.

The Application should allow users to:
1. Add items to the shopping list.
2.  Remove items from the shopping list.
3. Ask for help.
4. Show the items in the shopping list.

The application can be broken down into the following tasks:
1. Create a data structure that can store shopping list items.
2. Create a function to show a HELP menu to the user.
3. Create a function to ADD an item to the list
4. Create a function to REMOVE an item from the list.
5. Create a function  that display the shopping list to the screen.
6. Create a working shopping list program using a WHILE LOOP using your function created above.
"""
# Create a data structure that can store shopping list items.
shopping_list = []


# Create a function to show a HELP menu to the user.
def start_menu():
	print("What do you want to add to your shopping list?: ")
	print("""
	Enter 'DONE' to stop adding item.
	Enter 'HELP' for additional item.
	Enter 'SHOW' to see your shopping list.
	Enter 'REMOVE' to remove an item from your shopping list.
	-----------------------------------------------------------------------------
	""")


# Create a function to ADD an item to the list.
def add_to_list(item):
	item = item.capitalize()
	if item not in shopping_list:
		shopping_list.append(item)
		print(f"{item} was added to your shopping list.")
		print(f"You've {len(shopping_list)} item's on your shopping list.")
	else:
		print("This item is already on your list.")


# Create a function to DELETE an item from the list.
def remove_item(item):
	item = item.capitalize()
	if item in shopping_list:
		shopping_list.remove(item)
		print(f"{item} was removed from your shopping list.")
		print(f"You've {len(shopping_list)} item's on your shopping list.")
	else:
		print("This item is not on your list.")


# Create a function that display the shopping list to the screen.
def show_shopping_list():
	for item in shopping_list:
		print(item)


# Create a working Shopping List program using your function above.
start_menu()
while True:
	user_input = input("> ")
	if user_input == "DONE":
		start_menu()
		print("See you soon")
		break

	elif user_input == "HELP":
		start_menu()
		print("""
		Type an item into the box provided to add an item to your shopping list!""")
		continue

	elif user_input == "SHOW":
		start_menu()
		print("This is your Shopping List")
		show_shopping_list()
		continue

	elif user_input == "REMOVE":
		show_shopping_list()
		item = input("What do you want to remove: ")
		start_menu()
		remove_item(item)
		continue
	else:
		start_menu()
		add_to_list(user_input)
show_shopping_list()
