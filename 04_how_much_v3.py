""" Component 2 - How much v3
More efficient as contains valid range as basis of while loop removing the need
of the 'valid' variable
"""

error = "That was not valid input\n"
user_balance = 0

# Loop until valid input is entered (1-10)
while not 1 <= user_balance <= 10:
    try:
        # Ask for amount
        user_balance = int(input("Please enter whole number between 1 and 10"
                                 "\nHow much do you want to pay? $"))
        print()

    except ValueError:
        print(error)

print(f"You are playing with ${user_balance}")
