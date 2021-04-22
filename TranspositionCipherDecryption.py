#!/usr/bin/env python

import math

# http://inventwithpython.com/hacking (BSD Licened)

def main():
    myMessage = ''
    myKey = ''

    while myMessage:
        myMessage = input('Enter encrypted text:')

    while myKey:
        myKey = int(input('Enter your Key:'))
    
    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext + '|')

def decryptMessage(key, message):

    numOfColums = math.ceil(len(message) / key)

    numOfRows = key

    numOfShadedBoxes = (numOfColums * numOfRows) - len(message)

    plaintext = [''] * numOfColums

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColums) or (col == numOfColums - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

if __name__ == '__main__':
    main()



