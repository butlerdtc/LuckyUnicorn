""" Component 3 - Random token generator v1
Generates random choice of tokens in random order
"""

import random

tokens = ["horse", "donkey", "zebra", "unicorn"]

# Test loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # Can wrap output making screenshotting easier
    