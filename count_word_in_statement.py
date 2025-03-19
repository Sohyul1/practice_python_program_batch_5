# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

# Ask for user input
statement = input("Enter a complete statement: ")

# Use split to split the words
statement_count = len(statement.split())   # Count the words usinng len

# Print the number of words
print(statement_count)