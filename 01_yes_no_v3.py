"""Lucky Unicorn Yes/No Checker
Uses code from v2 and places it into a loop to make testing more efficient
"""


# Loop for code to make testing efficient
show_instructions = ""
while show_instructions != "1":
    # Ask user if they have played before
    show_instructions = input("Have you played the game before?: ").lower()

    # If yes output 'Program continues
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # If no output 'Show instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display Instructions")

    # Otherwise show 'Error'
    else:
        print("Please enter 'yes' or 'no'")
    # Test statement
    print(f"You entered '{show_instructions}'")
