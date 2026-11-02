
import random

passwordList = []

# Welcome the user to the password generator
print("Welcome to the Password Generator!")

# Define the characters that can be used in the password
smallCharacters = "abcdefghijklmnopqrstuvwxyz"
capitalCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numCharacters = "0123456789"
specialCharacter = "!@#$%^&*()_+~`|}{[]\\:;?><,./-="

# Ask the user how many characters of each type they want
smallChar = int(input("How many small characters would you like in your password? "))
capitalChar = int(input("How many capital characters would you like in your password? "))
numChar = int(input("How many numbers would you like in your password? "))
specialChar = int(input("How many special characters would you like in your password? "))

# Randomly select the requested number of lowercase characters
randomSmallChar = random.choices(smallCharacters, k=smallChar)

# Add the selected lowercase characters to the password list
passwordList += randomSmallChar

# Randomly select the requested number of uppercase characters
randomCapitalChar = random.choices(capitalCharacters, k=capitalChar)

# Add the selected uppercase characters to the password list
passwordList += randomCapitalChar

# Randomly select the requested number of numbers
randomNumChar = random.choices(numCharacters, k=numChar)

# Add the selected numbers to the password list
passwordList += randomNumChar

# Randomly select the requested number of special characters
randomSpecialChar = random.choices(specialCharacter, k=specialChar)

# Add the selected special characters to the password list
passwordList += randomSpecialChar

# Shuffle all the characters to make their order random
random.shuffle(passwordList)

# Convert the list into a string to create the final password
password = "".join(passwordList)

# Display the generated password
print(f"\nYour new password is: \n{password}")
