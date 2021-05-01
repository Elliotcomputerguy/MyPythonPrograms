#!/usr/bin/env python
import random

HANGMAN = (
    '''
 --------
 |      |
 |
 |
 |
 |
 |
 |
 |
 |
------------
''',
'''
 --------
 |      |
 |     ('')
 |
 |
 |
 |
 |
 |
 |
------------
''',
'''
 --------
 |      |
 |     ('')
 |    @-++-@
 |
 |
 |
 |
 |
 |
------------
''',
'''
 --------
 |      |
 |     ('')
 |    @-++-@
 |    |    
 |    +
 |
 |
 |
 |
------------
''',
'''
 --------
 |      |
 |     ('')
 |    @-++-@
 |    |    |
 |    +    +
 |
 |
 |
 |
------------
''',
'''
 --------
 |      |
 |     ('')
 |    @-++-@
 |    | || |
 |    + @@ +
 |
 |
 |
 |
------------
''',
'''
 --------
 |      |
 |     ('')
 |    @-++-@
 |    | || |
 |    + @@ +
 |     /  \\
 |    |
 |   <'   
 |
------------
''',
'''
 --------
 |      |
 |     ('')
 |    @-++-@
 |    | || |
 |    + @@ +
 |     /  \\
 |    |   |
 |   <'   '>
 |
------------
''',
)
MAX_WRONG = len(HANGMAN) -1

WORDS = ('ferrari','sneakers','domino pizza','computer','learning','python')

word = random.choice(WORDS)
so_far = '-' * len(word)

wrong = 0
used = []

print('Welcome to the Hangman Game. Good Luck!')

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print(f'\nYou have used the following letters:\n {used}')
    print(f'\nSo far, the word is:\n {so_far}')

    guess = input('\n\nEnter your guess: ')
    guess = guess.lower()

    while guess in used:
        print(f'\n\nYou already guessed the letter {used}')
        guess = input('\n\nEnter your guess: ')
        guess = guess.lower()
    used.append(guess)

    if guess in word:
        print(f'\nYes! {guess} is the Letter!')
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print(f'\nSorry {guess} is not the word')
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print('You have been hanged!')
else:
    print('You guessed it!')

print(f'The word was {word}')
input('Press any key to exit')
    
