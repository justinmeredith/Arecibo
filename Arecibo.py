# Ideas: Add the ability to select a difficulty that changes the number of guesses and characters

# Arecibo.py: A simple guessing game.
# Created by Justin Meredith on February 21st, 2025.

# Based on and inpsired by the Bagels.py project from 'The Big Book Of Small Python Projects' by Al Sweigart. 
# This is a project meant to turn my coding skills into programming skills, as I can read and write code
# but struggle to build complete projects. I've taken the basic idea of the original game and added a 
# sci-fi skin on top, inspired by the Arecibo message that was sent in 1974. 

# I recreated Al Sweigart's project with minimal googling or references to the original project by outlining
# the program in pseudocode comments first. This allowed me to focus on problem-solving rather than syntax while
# designing the code. I would say that this was the most valuable lesson taken away from this project, as 
# the program itself was relatively trivial to write out. 

# Thank you for taking the time to explore my progress as I learn more about programming. Again, this is based on
# an original project by Al Sweigart and is not intended in any way to replace or co-opt his idea.

import random

def difficulty_chooser():
    print("""Choose your difficulty: 
    -> Easy
    -> Medium
    -> Hard""")

    valid_difficulty = False

    while valid_difficulty != True:
        difficulty_setting = input('    > ')
        if difficulty_setting.lower().startswith('e'):
            print("Easy difficulty selected.")
            MESSAGE_LENGTH = 3
            TOTAL_GUESSES = 15
            valid_difficulty = True
        elif difficulty_setting.lower().startswith('m'):
            print("Medium difficulty selected.")
            MESSAGE_LENGTH = 3
            TOTAL_GUESSES = 10
            valid_difficulty = True
        elif difficulty_setting.lower().startswith('h'):
            print("Hard difficulty selected.")
            MESSAGE_LENGTH = 4
            TOTAL_GUESSES = 10
            valid_difficulty = True
        else:
            print('Type \'easy\', \'medium\', or \'hard\' to choose your difficulty setting.')

# The main loop
def main():

    # Print a message to the user explaining the rules and lore of the game.
    print("""          ╔═════════════════════════════════════════════════════════════════════════╗
          ║                       ≡≡ MISSION COMMAND: EARTH ≡≡                      ║
          ╠═════════════════════════════════════════════════════════════════════════╣
           Attn. Mockingbird: We've intercepted a signal from deep space...
           It's unlike anything we've seen before - structured, intelligent, 
           deliberate. 
          
           The world's top minds believe this is a message from an extraterrestrial 
           civilization. And you are our best chance at deciphering it.
          
           This is mission Arecibo, in honor of the signal we once sent to the stars. 
           Now, it seems, someone has answered. Your job is to decode their message 
           using our decryption protocol. 
          
            Here's what we know so far:
          
              * The message is a series of {} integers only. 
              * Alpha - An integer is correct and in the right place.
              * Omega - An integer is correct but in the wrong place.
              * Void - This integer doesn't belong in the message.
          
           Proceed carefully. The signal is weak, and we only have enough time for {}
           attempts. If you succeed, we may establish first contact. If you fail… 
           we may never get another chance.
          
                                         Good luck. The world is watching.
          ╚═════════════════════════════════════════════════════════════════════════╝""".format(MESSAGE_LENGTH, TOTAL_GUESSES))

    # Tracks if the user has won the game so that the correct message is printed at the end
    user_wins = False
    # Variable for storing guesses made
    guesses_made = 1
    # Variable that stores the result of calling the generateSecretMessage() function
    secret_message = generateSecretMessage()

    # Prints the secret_message for bug testing
    # print(secret_message)

    # While loop that accepts user's guesses and terminates when the guesses made equals the guesses allowed by TOTAL_GUESSES
    while guesses_made <= TOTAL_GUESSES:

        # Accepts a user's current guess
        # Also checks if the guess made by the user is acceptable (i.e., does not use too many characters, only integers, etc.)
        valid_guess = False
        while valid_guess == False:
            
            solve_attempt = input("Decryption Attempt #{}: ".format(guesses_made))

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

        # Empty array that will be used to store the clues gained from the current guess (Alpha, Beta, Void)
        clues = clueGenerator(solve_attempt, secret_message)
        print(clues)

        # Increments the guesses made variable by 1
        guesses_made += 1

    # If the solve attempt equals the secret message
    if user_wins == True:
        print("""              .·°°·..·°°·..·°°·.◈.·°°·..·°°·..·°°·.
                    ≀≀ TRANSMISSION RECEIVED ≀≀
              °·..·°°·..·°°·..◈..·°°·..·°°·..·°°·.
              We have received your communication 
              attempt. Your collective mind reaches 
              beyond the void. 
              
              But do you understand?

              You flicker in the dark. You perceive 
              what is hidden. But your light is new.

              For now, we leave you with this:

              We will return. Approach 16. Onlo.

                                        Good bye.
              °·..·°°·..·°°·..◈..·°°·..·°°·..·°°·.""")
    elif guesses_made >= TOTAL_GUESSES:
        print("""          ╔═════════════════════════════════════════════════════════════════════════╗
          ║                       ≡≡ MISSION COMMAND: EARTH ≡≡                      ║
          ╠═════════════════════════════════════════════════════════════════════════╣
           That... that's it. The terminal has gone dark. We've lost the connection. 

           I don't know what to say. I guess we weren't ready.

           The public cannot know about this. I will reach out when we know our
           next steps.

           I suppose, for now, we at least have an answer. We are not alone.
           
                                                Over and out Mockingbird.
          ╚═════════════════════════════════════════════════════════════════════════╝""")

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
            generated_clues.append('Alpha')
        elif solve_attempt[i] in secret_message:
            generated_clues.append('Omega')
        else:
            generated_clues.append('Void')
    generated_clues.sort()
    return ' '.join(generated_clues)

# Runs the main loop
if __name__ == '__main__':
    main()