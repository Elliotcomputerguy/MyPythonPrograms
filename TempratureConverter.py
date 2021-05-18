#!/usr/bin/env python
import sys

def convert_cel_to_far(c):
    f = c * 9/5 + 32
    evaluated = f'\nConversion: {f}'
    return evaluated

def convert_far_to_cel(f):
    c = (f - 32) * 5/9
    evaluated = f'\nConversion: {c}'
    return evaluated

def main():
    while True:
        print('''
                Temprature Converter
                 \ \ \ \ \ \ \ \ \ \ 

        [1] Convert from Celsius to Farnehiet
        [2] Convert from Farenheit to Celsius
        [3] Exit

        ''')
        menuOptions = (1, 2, 3,)
        menuChoice = ''
        while menuChoice not in menuOptions:
            try:
                menuChoice = int(input(':>'))
            except ValueError:
                print('Please enter a menu option')
        if menuChoice == 1:
            userCelciusConvert = ''
            while not userCelciusConvert:
                try:
                    userCelciusConvert = int(input('Enter a Celsius temprature to convert to Farneheit:'))
                    print(convert_cel_to_far(userCelciusConvert))
                except ValueError:
                    print('Please enter a integer value')
        elif menuChoice == 2:
            userFarneheitConvert = ''
            while not userFarneheitConvert:
                try:
                    userFarneheitConvert = int(input('Enter a Farenheit temprature to convert to Celsius:'))
                    print(convert_far_to_cel(userFarneheitConvert))
                except ValueError:
                    print('Please enter a integer value')
        elif menuChoice == 3:
            print('Exit application.')
            sys.exit()
main()