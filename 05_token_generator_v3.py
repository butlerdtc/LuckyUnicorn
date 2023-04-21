""" Component 3 - Random token generator v3
Gives house an advantage as less chance of user winning as less chance of
getting a unicorn token
"""

import random

tokens = ["unicorn",
          "horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey"]

STARTING_BALANCE = 100
balance = STARTING_BALANCE


# Test loop to generate 100 tokens
for item in range(100):
    token = random.choice(tokens)

    # Adjust user balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50

# Output
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
