# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# Ask for user input
name = input("Enter your name(with spaces at the beginning): ")

# Remove the spaces
print(name.lstrip()) # Print the output

