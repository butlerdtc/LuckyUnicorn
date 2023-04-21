""" Component 3 - Random token generator v2
Calculates user balance based on tokens generated
"""

import random

tokens = ["horse", "donkey", "zebra", "unicorn"]
balance = 100


# Test loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # Can wrap output making screenshotting easier

    # Adjust user balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50

    # Output
    print(f"Token: {token}, Balance: ${balance}")
