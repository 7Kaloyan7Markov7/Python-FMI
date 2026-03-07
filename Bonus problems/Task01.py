user_type = input("Enter a type: ")
args = input("Enter arguments: ")

result = None

if user_type == "int":
    result = int(args)

elif user_type == "str":
    result = args

elif user_type == "float":
    result = float(args)

elif user_type == "list[str]":
    result = [x.strip() for x in args.split(",")]

elif user_type == "list[int]":
    result = [int(x.strip()) for x in args.split(",")]
        

elif user_type == "dict[str]":
    result = {key.strip() : value.strip() for key, value in (pair.split(":",1) for pair in args.split(","))}

else:
    print(f"Invalid type {user_type}\n")

print(result)
