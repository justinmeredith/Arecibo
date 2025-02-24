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

    # Tracks if the user has won the game so that the correct message is printed at the end
    user_wins = False
    # Variable for storing guesses made
    guesses_made = 1
    # Variable that stores the result of calling the generateSecretMessage() function
    secret_message = generateSecretMessage()
    print(secret_message)

    # While loop that accepts user's guesses and terminates when the guesses made equals the guesses allowed by TOTAL_GUESSES
    while guesses_made <= TOTAL_GUESSES:

        # Accepts a user's current guess
        # Also checks if the guess made by the user is acceptable (i.e., does not use too many characters, only integers, etc.)
        valid_guess = False
        while valid_guess == False:
            
            solve_attempt = input("Encryption Attempt #{}: ".format(guesses_made))

            if len(solve_attempt) != MESSAGE_LENGTH:
                print('Your decryption can only be {} integers in length, as that is the length of the alien transmission.'.format(MESSAGE_LENGTH))
            elif solve_attempt.isdecimal() != True:
                print('Your decryption must consist of integers (0-9) only.')
            else:
                valid_guess = True

        # If the current solve attempt is the secret message, break from this while loop, user wins
        if solve_attempt == secret_message:
            user_wins = True
            break

        # Empty array that will be used to store the clues gained from the current guess (Prime, Beta, Void)
        clues = clueGenerator(solve_attempt, secret_message)
        print(clues)

        # For loop that runs MESSAGE_LENGTH times
            # Calls a function that checks the user's guess against the generated secret message
            # Stores the result of that function call (a clue) in the empty clues array

        # Sorts the clues array in alphabetical order to obscure which integer each clue word refers to
        # Prints the clues array as a string so the user can decide on their next guess

        # Increments the guesses made variable by 1
        guesses_made += 1
    
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
# Returns the clues as a sorted array to provide feedback without being too specific
def clueGenerator(solve_attempt, secret_message):
    # Array that will store and return the clues
    generated_clues = []

    for i in range(MESSAGE_LENGTH):
        if solve_attempt[i] == secret_message[i]:
            generated_clues.append('Prime')
        elif solve_attempt[i] in secret_message:
            generated_clues.append('Beta')
        else:
            generated_clues.append('Void')
    generated_clues.sort()
    return generated_clues

# Runs the main loop
if __name__ == '__main__':
    main()