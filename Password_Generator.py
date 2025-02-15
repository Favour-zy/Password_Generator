import random
import string

def generate_password():
    print("Password Generator")
    
    try:
        length = int(input("Enter password length: "))
        if length < 6:
            print("Password length should be at least 6 characters")
            return

        # Define character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine all characters
        all_characters = lowercase + uppercase + digits + symbols

        # Generate password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        
        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid number!")

generate_password()