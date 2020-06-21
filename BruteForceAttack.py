#!/usr/bin/python3

# Import the itertools.product which is similar to a for-loop in the generation of expression
from itertools import product

# Import the characters to be serched for
from string import ascii_letters, digits, punctuation

# Nominate the password to crack
# This can be changed to a larger charater set or SHA256 for example but for demo purposes 
# I have set it to 3 charaters long. If this is changed the range also need to be changed
passwordSimple = "a$2"

# Then create the character ist to be used for brute force
string = ascii_letters + digits + punctuation

# Set the lenght of password to brute force, in this case 3
for l in range(1,3):

# Repeat search scrollingthrough one letter or digit at a time
        for attempt in product(string, repeat=l + 1):

# Display the scrolling search
            print(f"Trying password {attempt}")

# provide output when the match is found
            if"".join(attempt) == passwordSimple:
                print(f"Password has been cracked! It was :", attempt)

# Break the search when the password has been cracked
                break