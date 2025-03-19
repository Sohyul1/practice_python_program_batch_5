# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# Ask for user input
name = input("Enter your name (in incorrect spacing): ")

# Convert to reverse case
print(name.swapcase())    # Print the name 
