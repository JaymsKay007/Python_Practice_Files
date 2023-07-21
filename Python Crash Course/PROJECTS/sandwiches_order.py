sandwich_order = ["Chicken Sandwich", "Egg Sandwich", "Ham Sandwich", "Nutella Sandwich", "Seafood Sandwich"]
finished_sandwiches = []
while sandwich_order:
    processing = sandwich_order.pop()
    print(f"They're now processing {processing.title()} in the kitchen.")

    finished_sandwiches.append(processing)
    print("The finished Sandwiches:")
    for finished_sandwich in finished_sandwiches:
        print(f"{finished_sandwich}. ")
