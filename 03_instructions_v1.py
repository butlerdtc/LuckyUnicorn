""" Uses function from 02_yes_no_function_v1 as base for new function
Which incorporates both yes/no checker and displays instructions
"""


# Yes/No checker function
def yes_no(question_text):
    while True:

        # Ask user if they have played before
        answer = input(question_text).lower()

        # If yes output 'Program continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If no output 'Show instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise show 'Error'
        else:
            print("Please enter 'yes' or 'no'")


# Display instructions function
def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# Main routine
played_before = yes_no("Have you played the game before? ")

if played_before == "No":
    instructions()
else:
    print("Program continues")
