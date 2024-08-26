def encrypt(text, shift):
    encrypted_text = []
    encrypted_position = -1
    encrypted_text_string = ""
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for position, item in enumerate(text):
        
        encrypted_position += 1
        text_position = alphabet.index(item)
        shift_position = text_position + shift
        # This will provide the remander when dividing by 25. % is modulo
        shift_position %= len(alphabet)

        encrypted_value = alphabet[shift_position]
    
        #Adding to the encrypted string just appends another letter.
        encrypted_text_string += encrypted_value

        #Originally used a list instead of a string, but we can just jump to using a string.
        #encrypted_text.insert(encrypted_position,encrypted_value)

        print(f"position {position} item {item} text_position {text_position} shift_position {shift_position} encrypted value {encrypted_value} ")
    
        #encrypted_text_string = ''.join(encrypted_text)

        print(f"encrypted text {encrypted_text} encrypted_text_string {encrypted_text_string}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction == "encode": 
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number\n"))
    encrypt(text, shift)
elif direction == 'decode':
    print("decode")


# TODO-1: Create a function called encrypt() that takes original text and shift_amount as 2 inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the original_text fowards in the alphabet by the shift_amount and primt the encrypted text.

# TODO-4: What happens if you try to shift z forward by 9? Can you fix the code

# TODO 3: Call the 'encrypt()' function and pass in the user inputs.  you should