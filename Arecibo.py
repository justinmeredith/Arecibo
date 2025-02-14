import random

message_length = 3
guesses_allowed = 10

def generateSecretMessage():
    numbers = list('1234567890')
    random.shuffle(numbers)
    