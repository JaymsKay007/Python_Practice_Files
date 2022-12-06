import random
# names = ["James", "Binta", "Dehwe", "Alpha", "Umar"]
names = input("Give everybody names, seperated by comma.?")
split_name = names.split(", ")
person_who_will_pay = random.choice(split_name)

print(f"{person_who_will_pay } is going to pay the bill today.")
