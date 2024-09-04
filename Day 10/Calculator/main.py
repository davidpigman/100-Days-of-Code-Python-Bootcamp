from art import logo

def add(n1, n2):
    return n1 + n2

# TODO 1: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO 2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

calculations = {}
continue_calc_loop = True
continue_calc_count = 0

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#print(f"calculations!! {calculations}")

# TODO 3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
print(logo)

while continue_calc_loop:
    continue_calc_count += 1

    if continue_calc_count == 1:
        first_number = float(input("What's the first number? "))
    else:
        if continue_calc == "y":
            first_number = output
        else:
            first_number = float(input("What's the first number? "))

    operation = input("Pick an operation ")
    second_number = float(input("What's the next number "))

    output = calculations[operation](first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {output}")

    continue_calc = input(f"Type 'y' to continue calculating with {output} or type 'n' to start a new calculation: ")

