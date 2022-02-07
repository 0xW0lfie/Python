#!/bin/python3

#Guess the Number
import random

secretNum = random.randint(1,20)
print("I'm thinking of a number between 1 and 20")

#Ask the player to make their 6 guesses
for guessTaken in range(1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < secretNum:
        print("Your guess is too low")
    elif guess > secretNum:
        print("Your guess is too high")
    else:
        break #Correct guess

if guess == secretNum:
    print('Good Job! You guessed my number in {} guesses!'.format(guessTaken))
else:
    print('Nope. The number I was thinking of was {}'.format(secretNum))
