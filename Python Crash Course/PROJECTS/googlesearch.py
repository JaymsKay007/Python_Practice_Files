# importing the search function from the pywhatkit library
from pywhatkit import search

# initializing a variable with the text that we want to search
query = input("What do you want to search for?: ")
# Displaying the text that we want to search
print(f"Searching for the query : {query}")
# searching the text using teh search() function
search(query)
