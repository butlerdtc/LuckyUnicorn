""" Component 4 - Game mechanics and looping v3
Based on 06_rounds_v1
Converting v2 into a function
"""

import random


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
starting_balance = 5
closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print("Goodbye")
