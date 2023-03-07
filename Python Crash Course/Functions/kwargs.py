def personal_info(**info):
    print(type(info))

    for key, value in info.items():
        print(f"The key {key} has a value {value}.")


print(personal_info(fn="james", ls="kay", age=30, hobby="coding"))
