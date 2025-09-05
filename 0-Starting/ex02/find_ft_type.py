def all_thing_is_obj(object: any) -> int:
    type_name = type(object).__name__
    if (type_name == "list"):
        print(f"List : {type(object)}")
    elif (type_name == "tuple"):
        print(f"Tuple : {type(object)}")
    elif (type_name == "set"):
        print(f"Set : {type(object)}")
    elif (type_name == "dict"):
        print(f"Dict : {type(object)}")
    elif (type_name == "str"):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42

