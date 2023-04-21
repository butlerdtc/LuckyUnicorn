""" LU base component - based on 00_LU_base_v1
Components get added after created and tested
"""
import random


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


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "X":
        rounds_played += 1  # Keeps track of rounds
        number = random.randint(1, 100)  # Can only be a donkey

        # Adjust balance
        # If the random number is between 1 and 5
        # User gets a unicorn (+ $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4

        # If the random number is between 6 and 36
        # User gets a donkey (- $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # In all other cases the token is a zebra/horse
        # (- $0.50 from balance)
        else:
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.5

            else:
                # All other cases horse token is generated
                token = "horse"
                balance -= 0.50

        # Output
        print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}"
              f"")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "X"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> "
                               "to "
                               "play again or 'X' to exit")
        print()
    return balance


# Main routine
played_before = yes_no("Have you played the game before? ")

if played_before == "No":
    instructions()

# Ask user how much they want to pay
starting_balance = num_check("How much would you like to pay? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print("Goodbye")
