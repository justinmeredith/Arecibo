import random

message_length = 3
guesses_allowed = 10

def main():
    print('The program is running.')
    secret_message = generateSecretMessage()
    print('The secret message is {}.'.format(secret_message))

def generateSecretMessage():
    numbers = list('1234567890')
    random.shuffle(numbers)

    secret_message = ''

    for i in range(message_length):
        secret_message += str(numbers[i])
    return secret_message

if __name__ == '__main__':
    main()