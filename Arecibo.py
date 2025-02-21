# Ideas: Add a scoring system, apply a sci-fi theme. This is a message coming from alien invaders that the player 
# needs to decode. 

import random

MESSAGE_LENGTH = 3
TOTAL_GUESSES = 5

def main():
    print('The program is running.')
    secret_message = generateSecretMessage()
    print('The secret message is {}.'.format(secret_message))

    guesses_made = 1

    while guesses_made <= TOTAL_GUESSES:
        print('Decryption attempt #{}'.format(guesses_made))
        guess = input('> ')
        guesses_made += 1
    
    print('You are out of guesses!')

def generateSecretMessage():
    numbers = list('1234567890')
    random.shuffle(numbers)

    secret_message = ''

    for i in range(MESSAGE_LENGTH):
        secret_message += str(numbers[i])
    return secret_message

if __name__ == '__main__':
    main()