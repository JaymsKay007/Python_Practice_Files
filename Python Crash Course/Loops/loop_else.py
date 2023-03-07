find_items = input("What do you want to buy from the store?: ")
shop_items = {"apples": 0.40,
              "bread": 1.10,
              "butter": 1.50,
              "grapes": 2.50,
              "mustard": 3.20,
              "chocolate": 5.00}
for items, prices in shop_items.items():
    if find_items == items:
        print(f"{items.title()} is available and it'll cost you ${prices}")
        break
else:
    print("We do not have this item's in our store. Thank you!!!")
