#!/bin/python3

#Rock Paper Scissors Game
import random, sys

print('-' * 50)
print('ROCK, PAPER, SCISSORS')
print('-' * 50)

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print ('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one: r, p, s, or q')

    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    computerNumber = random.randint(1, 3)
    if computerNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif computerNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif computerNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p':
        print ('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print ('You lose!')
        losses = losses + 1
