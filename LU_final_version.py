""" LU final version - based on 00_LU_base_v3
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
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount between $1 and $10, this will be what you "
          "play with")
    print()
    print("Then press <enter> to play. You will get a random token which will "
          "be either a horse, donkey, zebra, or unicorn.")
    print()
    print("It costs $1.00 to play a round but, depending on the token you "
          "will see if you win or lose money. These are the payout amounts:\n"
          "\tUnicorn: $5.00 (balance increases by $4.00\n"
          "\tHorse: $0.50 (balance decreases by $0.50\n"
          "\tZebra: $0.50 (balance decreases by $0.50\n"
          "\tDonkey: $0.00 (balance decreases by $1.00\n")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with "
          "more money than you started with.\n")

    print("*" * 50)
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
        print(formatter("~", f"Round {rounds_played}"))
        print()
        number = random.randint(1, 100)  # Can only be a donkey

        # Adjust balance
        # If the random number is between 1 and 5
        # User gets a unicorn (+ $4 to balance)
        if 1 <= number <= 5:
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

        # If the random number is between 6 and 36
        # User gets a donkey (- $1 from balance)
        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("#", "Bad luck, you got a donkey"))
            print()

        # In all other cases the token is a zebra/horse
        # (- $0.50 from balance)
        else:
            if number % 2 == 0:
                balance -= 0.5
                print(formatter("^", "You got a zebra, better luck next time"))
                print()

            else:
                # All other cases horse token is generated
                balance -= 0.50
                print(formatter("^", "You got a horse, better luck next time"))
                print()

        # Output
        print(f"Your balance is: ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "X"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> "
                               "to play again or 'X' to exit").upper()
        print()
    return balance


# Function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()

played_before = yes_no("Have you played the game before? ")

if played_before == "No":
    instructions()

# Ask user how much they want to pay
starting_balance = num_check("How much would you like to pay? $", 1, 10)
print(f"You are playing with ${starting_balance} Please <enter> to start")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
