# SaVannah Hussey
# UWYO COSC 1010
# 11/18/2024
# Lab 10
# Lab Section: 14
# Sources, people worked with, help given to: 
# your
# comments
# here

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

# Given function to hash passwords using SHA-256
def get_hash(to_hash):
    """Generate SHA-256 hash of a string."""
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

# Function to crack the password by comparing hashes
def crack_password():
    # Try to open the 'hash' file and read the hashed password
    try:
        with open('hash', 'r') as file:
            target_hash = file.read().strip()  # Read the hash and remove any extra whitespace/newlines
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
                password = line.strip()  # Remove leading/trailing whitespaces, including newlines
                hashed_password = get_hash(password)  # Hash the password
                if hashed_password == target_hash:  # Compare the hash with the target
                    print(f"Password found: {password}")
                    return  # Exit once the password is found
    except FileNotFoundError:
        print("Error: The 'rockyou.txt' file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the 'rockyou.txt' file: {e}")

# Calling the function to crack the password
crack_password()
