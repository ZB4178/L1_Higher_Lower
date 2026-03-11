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


#Main Routine
print()
print("⬆️⬆️⬆️ Welcome to the Higher Lower Game ⬇️⬇️⬇️")
print()

# Loop for testing purposes

want_instructions = yes_no("Would you like to see the instructions? ")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("Program continues")
