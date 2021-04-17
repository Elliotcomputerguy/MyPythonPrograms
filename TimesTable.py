#!/usr/bin/python

# My simple times table program

i = 1
timestable = input('Enter your times table of choice:')
timestable = int(timestable)
while i <=10:
    print('10 x', i, '=', i * timestable )
    i = i + 1
    