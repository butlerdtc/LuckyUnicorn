""" Component 2 - How much v1
Ask user for how much they want to pay and check that it is an integer
between 1 and 10. If true this becomes their balance
"""

# Ask user for input of how much they want to pay
user_balance = int(input("How much do you want to pay? (must be a whole number"
                         "between $1 and $10) $"))

# Loop to keep asking until valid input is entered
while not 1 <= user_balance >= 10:
    print("Please enter a whole number between 1 and 10")
    # ask for user input
    user_balance = int(input("How much do you want to pay? $"))

print(f"You are playing with a balance of ${user_balance}")
