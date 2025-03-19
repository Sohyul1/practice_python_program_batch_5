# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# Ask for user input
full_name = input("Enter your name in incorrect casing: ")

# Convert it to snake casing (probably using .lower and .replace)
full_name_snake_case = full_name.lower()

# Print the name
print(full_name_snake_case)