#!/usr/bin/python

# Reverse Cipher
# http:/inventwithpython.com/hacking (BSD Licensed)

# message will store the value from the input function call
message = input()
# translated variable will store the reversed value. It is currently set as a blank string. 
# It set to a blank string so it can be declared/defined.
translated = ''

# the below is an assignment statement and stores the evaluated expression from len(message) in the variable i.
# the Len() function accepts a string value argument and returns an integer value of how many characters are in the string
# the Len() function will start from 1 so when indexing from a returned value of the Len() function call you will need to either - 1 or
# uses slicing as slicing does not create out of range errors. In this program you cannot slice as it is not logical for the outcome we want.
i = len(message) - 1
# While i is greater or equal to 0 continue to index the string in variable message and wrte the index character into the variable translated
while i >=0:
    translated = translated + message[i]
    # minus 1 on each iteration so we work our way through the value of i untill it is equal to 0 
    i = i - 1

print(translated)
