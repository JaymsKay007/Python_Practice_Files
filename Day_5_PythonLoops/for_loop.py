names = ["James", "Binta", "Jamestina", "Joel", "Rashida"]
for name in names:
    print(name)

# Break Statement
for name in names:
    if name == "Joel":
        break
    print(name)
 
# Continue Statement
for name in names:
    if name == "Jamestina":
        continue
    print(name)
