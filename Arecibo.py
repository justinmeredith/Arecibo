# Ideas: Add a scoring system, apply a sci-fi theme. This is a message coming from alien invaders that the player 
# needs to decode. Could also add the ability to select a difficulty that changes the number of guesses and characters

import random

# Constants
MESSAGE_LENGTH = 3
TOTAL_GUESSES = 5

# The main loop
def main():
    # Print a message to the user explaining the rules and lore of the game. Include the length of the secret message and 
    # the number of guesses available to the user

    # Variable for storing guesses made
    # Variable that stores the result of calling the generateSecretMessage() function

    # While loop that accepts user's guesses and terminates when the guesses made equals the guesses allowed by TOTAL_GUESSES
        # Accepts the user's current guess and stores it in a variable
            # The length of the user's guess should be equal to the MESSAGE_LENGTH constant
            # It should only contain integers
            # It should be stored as a string

        # If the current guess equals the secret message, break from this while loop

        # Empty array that will be used to store the clues gained from the current guess (Prime, Beta, Void)
            # Should be returned in alphabetical order so that the user does not know which integers line up with each clue

        # For loop that runs MESSAGE_LENGTH times
            # Calls a function that checks the user's guess against the generated secret message
            # Stores the result of that function call (a clue) in the empty clues array

        # Sorts the clues array in alphabetical order to obscure which integer each clue word refers to
        # Prints the clues array as a string so the user can decide on their next guess

        # Increments the guesses made variable by 1
    
    # If the current guess equals the secret message
        # Print a message to the user letting them know that they won the game
        # Program terminates
    # Else if the guesses made equals TOTAL_GUESSES
        # Print a message letting the user know they have lost the game
        # Print the secret message. Earth is doomed. 
        # Program terminates. 

# Generates a random sequence of integers equal to the length of the MESSAGE_LENGTH constant
def generateSecretMessage():
    numbers = list('1234567890')
    random.shuffle(numbers)

    secret_message = ''

    for i in range(MESSAGE_LENGTH):
        secret_message += str(numbers[i])
    return secret_message

# Checks each integer of the current guess against each integer of the secret message in the same position
# Accepts the current guess and secret message as parameters
    # Array that will store and return the clues

    # For MESSAGE_LENGTH times
        # If current_guess[i] equals secret_message[i]
            # Append 'Prime' to the clues array
        # Else if current_guess[i] is in secret_message
            # Append 'Beta' to the clues array
        
        # If clues array has no length (empty)
            # Return 'Void'
        # Else
            # Return array of clues

# Runs the main loop
if __name__ == '__main__':
    main()