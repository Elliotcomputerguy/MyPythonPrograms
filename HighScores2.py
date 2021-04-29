#!/bin/usr/env python

scores = []

choice = None
while choice != '0':

    print('''
    
    High Scores 2.0

    0 - Quit
    1 - List Scores
    2 - Add a Score
    
    ''')

    choice = input('Enter a choice:')

    # Exit
    if choice == '0':
        print('Good Bye')
    
    # List scores
    elif choice == '1':
        print('High Scores\t')
        print('NAME\tSCORE')

        for entry in scores:
            #print(f'list = {scores}')
            score, name = entry #<-- assigns the elements from the list using a for loop. variable score gets assigned the 
        print(f'{name}\t{score}') # first value from the list. variable name second. Tuple unpacking.
            #print(f'list = {scores}')

    #Add a score
    elif choice == '2':
        name = input('what is the players name:')
        score = int(input('Enter a score:'))
        entry = (score, name) # <-- creates a tuple called entry
        scores.append(entry) # <-- uses method append to list scores.
        #print(f'list = {scores}') 
        scores.sort(reverse=True) #<-- reverses the list so highest number is on top.
        scores = scores[:5] #<-- blank slices list to only keep 5 elements 
        #print(f'list = {scores}')
    else:
        print('Is not a valid choice')
