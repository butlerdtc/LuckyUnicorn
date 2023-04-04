""" LU base component
Components get added after created and tested
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


# Number checking function
def num_check(question, low, high):
    error = "That was not valid input\n" \
            "Please enter number between {} and {}\n".format(low, high)

    # Loop until valid input is entered
    while True:
        try:
            # Ask for amount
            response = int(input(question))

            # Check for number in required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
played_before = yes_no("Have you played the game before? ")

if played_before == "No":
    instructions()

# Ask user how much they want to pay
user_balance = num_check("How much would you like to pay? $", 1, 10)
print(f"You are playing with ${user_balance}")
