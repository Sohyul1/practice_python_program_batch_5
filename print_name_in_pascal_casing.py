# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# Ask for user input
full_name = input("Enter your fullname in incorrect casing: ")

# Convert to pascal casing  
full_name = full_name.title().replace(" ", "")

# Print the name
print(full_name)
