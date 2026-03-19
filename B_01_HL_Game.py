import math
import random

# Checks user response to a question is yes/no (y/n) returns 'yes' or 'no'
def yes_no(question):
    while True:
        response = input(question).lower()

        # Checks user response, question
        # repeats if users dont answer yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please type yes or no")


def instructions():
    print("""

*** Instructions ***

To begin, choose the number of rounds and either customise 
the game parameters or go with the default game (Where the 
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without 
running out of guesses

 Good luck.

    """)

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


# Calculate the number of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts Here

# Initialize game values
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("⬆️⬆️⬆️ Welcome to the Higher Lower Game ⬇️⬇️⬇️")
print()

want_instructions = yes_no("Would you like to see the instructions? ")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# Ask users if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# Allow user to choose the high / low number
else:
    low_num = int_check("Low number? ")
    high_num = int_check("High number? ", low=low_num+1)

# Calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

secret = random.randint(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (Based on mode)
    if mode == "infinite":
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} (Infinite mode) 💿💿💿"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)

    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num,high_num)
    print("Pssst, Spoiler Alert!", secret) # Remove this later

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # Ask user to guess the number...
        guess = int_check("Guess: ", low_num, high_num, exit_code="xxx")

        # Check that they don't want to quit
        if guess == "xxx":
            # Set end_game to use so that the outer loop can be broken
            end_game = "yes"
            break

        # Check that the guess is not a duplicate
        if guess in already_guessed:
            print(f"❓❓ You've already guessed {guess}.  You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ❓❓")
            continue

        # If guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        # Add one to the number of guesses used
        guesses_used += 1

        # Compare the users guess to the secret number set up feedback statement

        # If we have guesses left...
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"❌❌ Too low, please try a higher number. "
                        f"You've uses {guesses_used} / {guesses_allowed} guesses ❌❌")

        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"❌❌ Too high, please try a lower number. "
                        f"You've uses {guesses_used} / {guesses_allowed} guesses ❌❌")

        # When the secret number is guessed, we have three different feedback
        # options (lucky / 'phew' / well done)
        elif guess == secret:

            if guesses_used == 1:
                feedback = "🍀🍀 Lucky!  You got it on the first guess! 🍀🍀"
            elif guesses_used == guesses_allowed:
                feedback = f"😅😅 Phew!  You got it in {guesses_used} guesses. 😅😅"
            else:
                feedback = f"🥳🥳 Well done!  You guessed the secret number in {guesses_used} guesses. 🥳🥳"

        # If there are no guesses left!
        else:
            feedback = "😢😢 Sorry - you have no more guesses.  You lose this round! 😢😢"
            guesses_used += 1

        # Print feedback to user
        print(feedback)

        # Additional feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1:
            print("\n💣💣💣 Careful - you have one guess left! 💣💣💣\n")

    print()

    # Round ends here

    # If user has entered exit code, end game
    if end_game == "yes":
        break

    rounds_played += 1

    # Add result to history
    history_feedback = f"Round {rounds_played}: {feedback}"
    history_item = f"Round: {rounds_played + 1} - {history_feedback}"

    game_history.append(history_item)

    # Add Guesses to all score
    all_scores.append(guesses_used)

    # Game history / Statistics area
if rounds_played > 0:
    # Calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output game statistics
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"Best: {best_score} | Worst: {worst_score} | Average: {average_score:.2f} ")
    print()


    # Ask user if they want to see their game history
    see_history = yes_no("\n🪶🪶🪶 Would you like to see the game history? 🪶🪶🪶 ")
    if see_history == "yes":
        for item in game_history:
            print(item)
    print()
    print("⬆️⬆️⬆️ Thanks for playing! ⬇️⬇️⬇️")

else:
    print("🐔🐔🐔 Chickening out already? Yikes... 🐔🐔🐔")