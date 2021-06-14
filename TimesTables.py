# my shit multiplier app
def timesTable(multiplier, integer):
    ''' pass the function a multiplier and a intger to multiply '''
    value = multiplier * integer
    evaluatedExpression = f'{multiplier} * {integer} = {value}'
    return evaluatedExpression

def main():
    import sys
    ''' main program'''

    while True:
        integer = ''
        multiplier = ''

        while not multiplier:
            print('\n\tEnter any number to multiply.\n \tType exit to escape.\n')
            multiplier = input('Enter a multiplier:').lower().strip()
            if multiplier == 'exit':
                sys.exit()
            elif multiplier.isdigit():
                intMultiplier = int(multiplier)
            else:
                print('Please enter a number or exit to exit.')
        while not integer:

            integer = input('Enter a number to multiply:').lower().strip()
            if integer == 'exit':
                sys.exit()
            elif integer.isdigit():
                intInteger = int(integer)
            else:
                print('Please enter a number or exit to exit.')
        print(timesTable(intMultiplier, intInteger))

if __name__ == '__main__':
    main()
