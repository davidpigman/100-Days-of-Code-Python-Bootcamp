#Original working solution not optimized with functions
def format_name(first_name, last_name):
    first_name_len = len(first_name)
    last_name_len = len(last_name)
    first_name_typecase = ""
    last_name_typecase = ""

    for position, letter in enumerate(first_name):
        if position == 0:
            first_name_typecase += first_name[0].upper()
        else:
            first_name_typecase += first_name[position].lower()

        print(f"first_name_typecase {first_name_typecase} {position}")

    for position, letter in enumerate(last_name):
        if position == 0:
            last_name_typecase += last_name[0].upper()
        else:
            last_name_typecase += last_name[position].lower()

    full_name = first_name_typecase + " " + last_name_typecase
    
    return full_name


first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

full_name = format_name(first_name, last_name)
print(f"Your typecase formatted full name is {full_name}")
