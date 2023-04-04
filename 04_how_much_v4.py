""" Component 2 - How much v4
Changed v3 into a function
Made 'user_balance' variable to more generic name 'response' so it can be
reused elsewhere. The number range comparison had to be changed so function
can be used elsewhere
"""


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


# Main routine
user_balance = num_check("How much would you like to pay? $", 1, 10)
print(f"You are playing with ${user_balance}")
