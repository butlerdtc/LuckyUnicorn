""" Component 3 - Random token generator v4
Uses percentages to calculate tokens to ensure the house has an advantage
A 5% chance for unicorn, a 30% chance for donkey, and a 65% chance for zebra/
horse
"""

import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE


# Test loop to generate 100 tokens
for item in range(10):
    number = random.randint(1, 100)

    # Adjust user balance
    # If number between 1 and 5 it is a unicorn token
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    # If number between 6 and 36 it is a donkey token
    elif 6 < number <= 36:
        token = "donkey"
        balance -= 1

    # If token is not donkey or unicorn it is either horse or zebra so users
    # loses $0.50 anyway
    else:
        # If number is even set token to zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.50

        else:
            # All other cases token generated is horse
            token = "horse"
            balance -= 0.50

    # Output
    print(f"Token: {token}, Balance: ${balance:.2f}")

print()
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
