#!/usr/bin/python

# Ceasar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

# Decide on a key from 1 to 25. This is your encryption/decryption key.
# Find the plaintext letter's number.
# Add the key to the plain text letter's number.
# If this number is larger than 26, subtract 26.
# Find the letter for the number you've calculated. This is the ciphertext letter.
# Repeat steps 2 to 5 for every letter in the plaintext message.

# the string to be encrypted/decrypted
message = input('Enter message to encrypt or decrypt:')
# the encryption/decryption key
key = 25

# while statement to ensure that the end user does not go over 25 when selecting a key
while key >=25:
    key = input('Enter your encryption key up to 25:')
    # convert string into integer 
    key = int(key)

# asks the user which mode to select encryption/decryption
mode = input('Enter Encrypt to Encrypt or Decrypt to decrypt:')
# capatalize string
mode = mode.upper()

# every possible symbol that can be encrypted 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# variable for the encrypted/decrypted form of the message
translated = ''

# capatalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'ENCRYPT':
            num = num + key
        elif mode == 'DECRYPT':
            num = num - key

        # handle the wrap-around if num is larger than the length of LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted/decrypted numbers symbol at the end of translated
        translated = translated + LETTERS[num]
    else:
        # add the symbol without encryption/decryption
        translated = translated + symbol
        
if mode == 'DECRYPT':
    # print decrypted message
    print('Decrypted Message: ', translated)
elif mode == 'ENCRYPT':
    # print encrypted message
    print('Encrypted Message: ', translated)
    


