import random

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    # Create the character pool based on user preferences
    char_pool = lowercase_letters
    if use_uppercase:
        char_pool += uppercase_letters
    if use_digits:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars

    # Ensure we have enough types of characters to meet the length requirement
    if len(char_pool) < length:
        raise ValueError("Character pool is smaller than the desired password length.")

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

length = 16
password = generate_password(length)
print(f"Generated Password: {password}")
