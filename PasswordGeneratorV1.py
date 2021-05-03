#!/usr/bin/env python
#                                             #
#                                             #
# My first Python program 03-05-2021    :)    #
# Password Generator Version 1                #
# Author Elliot Stenning: ElliotComputerGuy   #
#                                             #
###############################################

def passwordCreator():
    ''' Generate a chosen amount of randomized passwords with the choice of password length '''
    print('''
        
██████   █████  ███████ ███████ ██     ██  ██████  ██████  ██████       ██████  ███████ ███    ██ ███████ ██████   █████ ████████  ██████  ██████  
██   ██ ██   ██ ██      ██      ██     ██ ██    ██ ██   ██ ██   ██     ██       ██      ████   ██ ██      ██   ██ ██   ██   ██    ██    ██ ██   ██ 
██████  ███████ ███████ ███████ ██  █  ██ ██    ██ ██████  ██   ██     ██   ███ █████   ██ ██  ██ █████   ██████  ███████   ██    ██    ██ ██████  
██      ██   ██      ██      ██ ██ ███ ██ ██    ██ ██   ██ ██   ██     ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██   ██    ██    ██ ██   ██ 
██      ██   ██ ███████ ███████  ███ ███   ██████  ██   ██ ██████       ██████  ███████ ██   ████ ███████ ██   ██ ██   ██   ██     ██████  ██   ██ 
        
        ''')

    userPasswordLength = int(input(' [+] Please enter the length size 0 - 50:>'))
    userGeneratedPasswords = int(input(' [+] How many passwords would you like to create:>'))
    userPassList = [jumbleWord(userPasswordLength) for _ in range(userGeneratedPasswords)]
    generatedPasswordList = f' [+] Your list has been created using {userPasswordLength} as your pass length\n\n {userPassList}'
    return generatedPasswordList

def jumbleWord(lengthNumber):
    ''' jumbleWord creates a random string from the character set abcdefghijklmnopqrstuvwxyz1234567890!"£$%&*()@?~#:;
        The function expects an integer argument to return a string length. 
        Example: jumbleWord(10) will return a randomized string size of 10 characters from the above character set. 
    '''
    import random
    passLength = lengthNumber
    jumbledWord = ''
    CHARACTERS = 'abcdefghijklmnopqrstuvwxyz1234567890!"£$%&*()@?~#:;'
    for characters in CHARACTERS:
        randomizer = random.choice(CHARACTERS)
        if len(jumbledWord) < passLength:
            jumbledWord += randomizer
    return jumbledWord

print(passwordCreator())