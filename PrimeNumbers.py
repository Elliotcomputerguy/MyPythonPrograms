
def primeNumbers(maxCount, file):
    # import pathlib, sys and time modules
    import pathlib
    ''' Count as many Prime numbers as you like, just give me a number to count to and a file to write to. ''' #<-- Doc String 
    # initalize variables
    iterator = 2 # iterator in while loop for prime 
    primeList = [] # prime number list
    compositeList = [] # non prime number list
    # create absolute path
    path = pathlib.Path.home() / file
    # check if file exists. If user does not change value of file then use default parameter value.
    if path.exists():
        # if user does not specify a maxCount value. use default parameter value of 100.
        while iterator <= maxCount:
            # when you mod by 2 it only evaluates to either a 0 or 1.
            # If it is a 0 it is not prime. If it is 1 it is prime.
            if iterator % 2 == 0:
                compositeList.append(iterator)
                iterator += 1
            else:
                primeList
                primeList.append(iterator)
                iterator += 1
        # insert -1 into the list on every iteration of 10 with for loop
        for i in range(0, maxCount, 11):
            primeList.insert(i, -1)
        # convert list into string and repalce -1 with a new line break and remove commas and brackets.
        primeList = ''.join(str(primeList)).replace('-1', '\n').replace(',', '').replace('[', '').replace(']','').strip()
        # insert -1 into the list on every iteration of 10
        for i in range(0, maxCount, 11):
            compositeList.insert(i, -1) 
        # convert list into string and repalce -1 with a new line break and remove commas and brackets.
        compositeList = ''.join(str(compositeList)).replace('-1', '\n').replace(',', '').replace('[', '').replace(']','').strip()
        with path.open(mode='w', encoding='utf-8') as fileObject:
            fileObject.write(f'\n\t\tPrime Numbers\n\n{primeList}\n\n\t\tComposite\n\n{compositeList}')
            completed = f'[+] prime numbers and composite numbers have been created up to {maxCount}'
        return completed
    else:
        return f'[-] Could not locate {file}. Exiting...'
        

def userPrimeMenu():
    # import modules
    import sys, time, pathlib, os
    # main body loop
    while True:
        os.system('cls')
        # initalize variables
        menuOption = (0, 1,) # Tuple for menu option
        confirmMenuOption = '' # user input variable
        #while menu loop if userinput is incorrect
        while confirmMenuOption not in menuOption:
            os.system('cls')
            # if user does not enter integer capture ValueError traceback
            try:
                # menu
                print(''' 
                \t\t Prime Calculator \n 
                [0] - Get a list of prime numbers and composite numbers
                [1] - Exit the application
                ''')
                confirmMenuOption = int(input('Enter menu option :>'))
            except ValueError:
                print('You did not enter a menu number.')

        if confirmMenuOption == menuOption[0]:
                # if user does not enter integer capture ValueError traceback
            confirmNumber = input('Enter a max number to count too or leave blank to use default:>')
            if confirmNumber == '':
                confirmNumber = int(100)
            else:
                confirmNumber = int(confirmNumber)
            confirmFile = input('Enter a filename with suffix to save to or hit enter to use default:>')
            # if default create default file
            if confirmFile == '':
                confirmFile = 'PrimeNumbers.txt'
                path = pathlib.Path.home() / confirmFile
                path.touch()
                if path.exists():
                    print(f'[+] {confirmFile} created.')
            else:
                # if not default create file of users choice
                path = pathlib.Path.home() / confirmFile
                path.touch()
                if path.exists():
                    print(f'[+] {confirmFile} created.')

            print(f'[+] {confirmNumber} added.')
            time.sleep(2)
            print(f'[+] file can be located at {path}')
            time.sleep(2)
            print(primeNumbers(confirmNumber, confirmFile))
            #read file
            with path.open(mode='r', encoding='utf-8') as fileObject:
                for lines in fileObject.readlines():
                    print(lines.strip())
                time.sleep(10)

        elif confirmMenuOption == menuOption[1]:
            print('Menu option 1 entered. Exiting program.')
            time.sleep(5)   # Delays for 5 seconds.
            sys.exit()
                     
userPrimeMenu()