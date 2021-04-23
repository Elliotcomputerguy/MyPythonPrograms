#!/usr/bin/env python
import random, os, sys
def main():
   # while True:

    WORDS = ('bobob', 'wimpy', 'burgerking', 'mcdonalds', 'kentuckyfriedchicken')
    lenWord = random.randrange(len(WORDS))
    word = WORDS[lenWord]
    print('original word var =', word)
    correct = word
    jumbledWord = ''

    while word:

        wordPosition = random.randint(0, len(word)) -1 #<-- randomise the value of word and assign to variable
        print('WordPosition from word =', wordPosition)
        jumbledWord += word[wordPosition] #<-- concatenate the index of word and assign to variable
        print('Jumbledword variable =', jumbledWord)
        word = word[:wordPosition] + word[(wordPosition + 1):] #<--Blank slice 
        print('Original word =', word)

    print('''

 ''')
    print('The jumbled word is: %s' % (jumbledWord))
    playerGuess = input('\nEnter your guess:').strip().lower()
    while playerGuess != correct and playerGuess != '':
        print('Sorry, that is not correct')
        playerGuess = input('Enter your guess:')

    if playerGuess == correct:
        print('You have guessed correctly\n')


main()




