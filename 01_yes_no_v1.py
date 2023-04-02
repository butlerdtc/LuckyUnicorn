""" V1 of code for Yes/No Checker
"""


# Ask user if they have played before
show_instructions = input("Have you played the game before?: ")

# If yes output 'Program continues
if show_instructions == "yes":
    print("Program continues")

# If no output 'Show instructions'
elif show_instructions == "no":
    print("Display Instructions")

# Otherwise show 'Error'
else:
    print("Please enter 'yes' or 'no'")
