#!/usr/bin/env python

def main():
    myMessage = input('Enter message:')
    myKey = int(input('Enter encryption key:'))

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

def encryptMessage(key, message):

    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):

            ciphertext[col] += message[pointer]

            pointer += key
    
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()