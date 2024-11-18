# SaVannah Hussey
# UWYO COSC 1010
# 11/18/2024
# Lab 10
# Lab Section: 14
# Sources, people worked with, help given to: Textbook Chapter: 8, 10
# COSC1010_lec11-Functions.pptx.pdf,COSC1010_lec13-FilesAndExceptions.pptx.pdf
# https://docs.python.org/3/tutorial/errors.html (where I learned use "except Excetption as e:"" block)
# Online tutor, 
#  ChatGPT, "give me tips on opening the file to get the target , 
# then opening and reading txt file to hash each password and 
# comparing it with the target , using try-except blocks for error handling (no code) " 
# 11/16/2024


#import modules you will need

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

from hashlib import sha256
from pathlib import Path


def get_hash(to_hash):
    """Generate SHA-256 hash of a string."""
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

#Created a function to crack the password by comparing hashes
def crack_password():
    try:
        with open('hash', 'r') as file:
            target_hash = file.read().strip()  
    except FileNotFoundError:
        print("Error: The 'hash' file was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the 'hash' file: {e}")
        return
    
    # Try to open the 'rockyou.txt' file containing possible passwords
    try:
        with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as password_file:
            for line in password_file:
                password = line.strip()  
                hashed_password = get_hash(password)  
                if hashed_password == target_hash:  
                    print(f"Password found: {password}")
                    return  
    except FileNotFoundError:
        print("Error: The 'rockyou.txt' file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the 'rockyou.txt' file: {e}")

crack_password()
