#!/bin/usr/env python

def milesToKilometers(miles):
    userMiles = miles
    miles *= 1.61
    conversion = round(miles, 2)
    milesToKilo = f'{userMiles}, miles is, {conversion} kilometers'
    return milesToKilo

def kiloToMiles(kilo):
    userKilo = kilo
    kilo /= 1.61
    conversion = round(kilo, 2)
    kiloToMiles = f'{userKilo} kilometers is {conversion} miles'
    return kiloToMiles

def main():
    import time, sys, os
    while True:
        os.system('cls')
        print(
        '''
        [1] - Convert miles to kilometers 
        [2] - Convert kilometers to miles
        [3] - Exit
        '''
            )
        optionMenu = (1,2,3)
        userChoice = None
        while userChoice not in optionMenu:
            try:
                userChoice = int(input('>'))
            except ValueError:
                print('Enter a number from the menu!')

            if userChoice == 1:
                try:
                    miles = float(input('Enter miles:'))
                    print(milesToKilometers(miles))
                    time.sleep(5)
                except ValueError:
                    print('Enter a number!')

            if userChoice == 2:
                try:
                    kilo = float(input('Enter kilos:'))
                    print(kiloToMiles(kilo))
                    time.sleep(5)
                except ValueError:
                    print('Enter a number!')

            if userChoice == 3:
                sys.exit()

if __name__ == '__main__':
    main()