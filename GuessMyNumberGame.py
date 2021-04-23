#!/usr/bin/env python

# This can be cleaned up and the flow can be made better.

import random, sys, os, time

def main():
    os.system('cls')
    print('''

 ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                                                                                         
\t\t\t\tWelcome to the guess the number game. Pick a number between 1 and 100. To exit type exit.
    ''')
    randomNumber = random.randint(1, 100)
    playerGuesses = 1
    while True:
        playerGuess = input('Guess a number between 1 and a 100:')
        playerExit = playerGuess.upper()
        if playerExit == 'EXIT':
            print('\nThanks for playing the Guess The Number Game')
            time.sleep(6)
            sys.exit()
        else:
            playerGuess = int(playerGuess)
        while playerGuess != randomNumber:
            if playerGuess > randomNumber:
                print('Your guess %s is to high' % (playerGuess))
            elif playerGuess < randomNumber:
                print('Your guess %s is to low' % (playerGuess))
            playerGuess = input('Guess a number between 1 and a 100:')
            playerGuess = int(playerGuess)
            playerGuesses += 1
        print('\nYou have guessed the number %s it took you %s guesses ' % (playerGuess, playerGuesses))
        time.sleep(6)
main()       
