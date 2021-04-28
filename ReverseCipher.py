#!/usr/bin/python

# Reverse Cipher
# http:/inventwithpython.com/hacking (BSD Licensed)

# message will store the value from the input function call
message = input()
# translated variable will store the reversed value. It is currently set as a blank string. 
# It set to a blank string so it can be declared/defined.
translated = ''

i = len(message) - 1
# While i is greater or equal to 0 continue to index the string in variable message and wrte the index character into the variable translated
while i >=0:
    translated = translated + message[i]
    # minus 1 on each iteration so we work our way through the value of i untill it is equal to 0 
    i = i - 1

print(translated)
