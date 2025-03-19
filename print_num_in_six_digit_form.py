# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# Ask for user input
num = input("Enter a number from 0-1000: ")

# Add zeros and print
print(num.zfill(6))