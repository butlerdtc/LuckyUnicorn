""" Component 2 - How much v2
Use try/accept to pull error message out of loop
"""

error = "Please enter a whole number between 1 and 10\n"
valid = False

# Loop until valid input is entered
while not valid:
    try:
        # Ask for amount
        user_balance = int(input("How much do you want to pay? $"))

        # Check if amount is too high/low
        if 0 < user_balance <= 10:
            print(f"You are playing with ${user_balance}")
            valid = True
        else:
            print(error)
    except ValueError:
        print(error)
