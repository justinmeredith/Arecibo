# Ideas: Add a scoring system, apply a sci-fi theme. This is a message coming from alien invaders that the player 
# needs to decode. 

import random

message_length = 3
guesses_remaining = 10

def main():
    print('The program is running.')
    secret_message = generateSecretMessage()
    print('The secret message is {}.'.format(secret_message))

    while guesses_remaining > 0:
        print('Decryption attempt #{}'.format(guesses_remaining))
        guess = input('> ')
        guesses_remaining -= 1

def generateSecretMessage():
    numbers = list('1234567890')
    random.shuffle(numbers)

    secret_message = ''

    for i in range(message_length):
        secret_message += str(numbers[i])
    return secret_message

if __name__ == '__main__':
    main()