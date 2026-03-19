# Checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
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


# Guessing loop

# replace number below with random number between high / low values
secret = 7

# parameters that already exist in base game
low_num = 0
high_num = 10
guesses_allowed = 5

# Set guess used to zero at the start of the round
guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    # Ask user to guess the number...
    guess = int_check("Guess: ", low_num, high_num)

    # Check that they don't want to quit
    if guess == "xxx":
        # Set end_game to use so that the outer loop can be broken
        end_game = "yes"
        break

    # Check that the guess is not a duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}.  You've *still* used "
              f"{guesses_used} / {guesses_allowed} guesses ")
        continue

        # If guess is not a duplicate, add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    # Add one to the number of guesses used
    guesses_used += 1

    # Compare the users guess to the secret number set up feedback statement

    # If we have guesses left...
    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low, please try a higher number. "
                    f"You've uses {guesses_used} / {guesses_allowed} guesses")
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, please try a lower number. "
                    f"You've uses {guesses_used} / {guesses_allowed} guesses")

    # When the secret number is guessed, we have three different feedback
    # options (lucky / 'phew' / well done)
    elif guess == secret:

        if guesses_used == 1:
            feedback = "🍀🍀 Lucky!  You got it on the first guess! 🍀🍀"
        elif guesses_used == guesses_allowed:
            feedback = f"Phew!  You got it in {guesses_used} guesses."
        else:
            feedback = f"Well done!  You guessed the secret number in {guesses_used} guesses."

    # If there are no guesses left!
    else:
        feedback = "Sorry - you have no more guesses.  You lose this round!"

    # Print feedback to user
    print(feedback)

    # Additional feedback (warn user that they are running out of guesses)
    if guesses_used == guesses_allowed - 1:
        print("\n💣💣💣 Careful - you have one guess left! 💣💣💣\n")

print()
print("End of round")