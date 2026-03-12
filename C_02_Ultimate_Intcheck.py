def int_check(question, low=None, high=None, exit_code=None):

    # If any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # If the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # If the number needs to be between low and high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # Check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer isn't too low...
            if low is not None and response < low:
                print(error)

            # Check the integer isn't too low...
            elif high is not None and response > high:
                print(error)

            # If response is valid, return it
            else:
                return response

        except ValueError:
            print(error)

# Main routine goes here

# rounds = "test"
# while rounds != "":
#     rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="")
#     print(f"You asked for {rounds}")

# low_num = int_check("Low number? ")
# print(f"You chose a low number of {low_num}")

# high_num = int_check("High number? ", low=1)
# print(f"You chose a high number of {high_num}")

# Check user guesses
guess = ""
while guess != "xxx":
    guess = int_check("Guess: ", low=0, high=10, exit_code="xxx")
    print(f"You guessed {guess}")
    print()