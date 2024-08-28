#Original working solution not optimized with functions
def format_name(name):
    name_len = len(name)
    name_typecase = ""

    for position, letter in enumerate(name):
        if position == 0:
            name_typecase += name[0].upper()
        else:
            name_typecase += name[position].lower()
        
        #Debugging Statement
        #print(f"name_typecase {name_typecase} {position}")

    return name_typecase

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

first_name_typecase = format_name(first_name)
last_name_typecase = format_name(last_name)

full_name = first_name_typecase + " " + last_name_typecase
print(f"Your typecase formatted full name is {full_name}")
