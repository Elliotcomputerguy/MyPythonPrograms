#!/usr/bin/python

def main():
    myMessage = input('Enter message:')
    myKey = input('Enter encryption key:')
    myKey = int(myKey)

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
