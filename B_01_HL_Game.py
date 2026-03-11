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



# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer more than / equal to 1"

        to_check = input(question)

        # checks for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts Here

# Initialize game values
mode = "regular"
rounds_played = 0


print("⬆️⬆️⬆️ Welcome to the Higher Lower Game ⬇️⬇️⬇️")
print()

want_instructions = yes_no("Would you like to see the instructions? ")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} (Infinite mode) 💿💿💿"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # If users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game history / Statistics area