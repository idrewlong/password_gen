import random
import string

# This Python function, generate_password, takes a minimum length and optional boolean parameters for including numbers and special characters, allowing users to customize the criteria for generating a password.

def generate_password(min_Length, numbers=True, special_characters=True):
        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation
        
        #concatenates a string of letters with digits and special characters based on boolean flags for including numbers and special characters. 
        
        characters = letters
        if numbers:
                characters += digits
        if special_characters:
                characters += special
                
        # This code initializes an empty string for a password (pwd) and sets boolean flags (meet_criteria, has_number, and has_special) to track whether the password meets certain criteria, including the presence of numbers and special characters.

        pwd = ""
        meet_criteria = False
        has_number = False
        has_special = False
        
        # This code generates a password in a loop until it meets specified criteria, ensuring the length is at least min_Length and includes numbers and/or special characters based on boolean flags, tracking the presence of numbers and special characters in the process.
        
        while not meet_criteria or len(pwd) < min_Length:
                new_char  = random.choice(characters)
                pwd += new_char
                
                if new_char in digits:
                        has_number = True
                elif new_char in special:
                        has_special = True
                        
                meet_criteria = True
                if numbers:
                        meet_criteria = has_number
                if special_characters:
                        meet_criteria = meet_criteria and has_special
        return pwd
                        
# This code prompts the user to input the minimum length and whether they want numbers and special characters in the password, then generates a password using the generate_password function with the specified criteria and prints the result.

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password:", pwd)