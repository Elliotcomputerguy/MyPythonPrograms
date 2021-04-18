#!/usr/bin/python

# Ceaser cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = input('Enter encrypted Ceaser cipher:')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('### Running decryption on all possible keys ###')
# Loop through every possible key
for key in range(len(LETTERS)):
    # It is important to set translated to a blank string so that the 
    # previous iteration's value for translated is cleared.
    translated = ''
    # run the decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # Get the number of the symbol
            num = num - key
            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)
            # add number's symbol at the end of translated    
            translated = translated + LETTERS[num]
        else:
            # add the symbol without encrypting/decrypting
            translated = translated + symbol
    # display the current key being tested, along with its decryption        
    print('Key #%s: %s' % (key, translated))
print('### Completed running through all decryption keys ###')
