#!/usr/bin/env Python

scores = []
choice = None
while choice != '0':
    print('''
    
    High Scores

    0 - Exit
    1 - Show Scores
    2 - Add a Score
    3 - Delete a Score
    4 - Sort Scores
    ''')

    choice = input('Enter a choice:')
    
    #Exit
    if choice == '0':
        print('Good Bye')

    #List high score table
    elif choice == '1':
        print('High Scores')
        for score in scores:
            print(score)
    
    #Add a score
    elif choice == '2':
        score = int(input('What score did you get:'))
        scores.append(score)

    #remove score
    elif choice == '3':
        score = int(input('Remove which score:'))
        if score in scores:
            scores.remove(score)
        else:
            print(f'{score} is not in the high scores list.')
        
    elif choice == '4':
        scores.sort(reverse=True)
        