# Simple Password Generator
# This simple project makes a random password with random letters and characters

import random # Used to generate random characters
import string

length = int(input('Enter the length of password')) # Uses the desired numbers of characters the user inputs

# Is use to make the characters and symbols
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols # Combines letters, numbers and symbols to be used

temp = random.sample(all,length) # Selects random characters from the full pool of letters, numbers, and symbols
password = "".join(temp) # Converts the list of characters into a single string
print(password) # Generates the randomized password
