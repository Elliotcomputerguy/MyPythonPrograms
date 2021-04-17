#!/usr/bin/python

# My Times table program

i = 1
print('Enter your times table of choice')
timestable = input()
timestable = int(timestable)
while i <=10:
    print('10 x', i, '=', i * timestable )
    i = i + 1