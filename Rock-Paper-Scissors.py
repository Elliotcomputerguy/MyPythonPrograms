
def gameTitle():

    title = print('''

██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗     ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
██║  ██║╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

    ''')

def gameRules(userArg, randArg):

    if randArg == 'rock':
        randArg = 1
    elif randArg == 'paper':
        randArg = 2
    elif randArg == 'scissors':
        randArg = 3

    if userArg == randArg or randArg == userArg:
        print('none')
        return None
    elif userArg == 1 and randArg == 2:
        player = 'player'
        return player
    elif randArg == 1 and userArg == 2:
        computer = 'computer'
        return computer
    elif userArg == 1 and randArg == 3:
        computer = 'computer'
        return computer
    elif randArg == 1 and userArg == 3:
        player = 'player'
        return player
    elif userArg == 2 and randArg == 3:
        computer = 'computer'
        return computer
    elif randArg == 2 and userArg == 3:
        player = 'player'
        return player

def main():
    import sys, random
    player = 0
    computer = 0
    options = [1,2]
    userMenuOption = None
    words = ['rock','paper','scissors']

    while True:
        print(gameTitle())

        print('''
                                             =========================================
                                              [1] - Play Rock Paper Scissors
                                              [2] - Exit
                                             =========================================
            ''')
        
        while userMenuOption not in options:
            try:
                userMenuOption = int(input('>'))
            except (ValueError):
                print('Select menu option')

            if userMenuOption == options[0]:
                print(gameTitle())
                while player or computer != 1:
                    print('\n\t\t Enter 1 for Rock, 2 for Paper, 3 for Scissors or E for exit')
                    playerMove = int(input('Enter Rock Paper or Sicssors >'))
                    if playerMove == 'e':
                        sys.exit()
                    else:
                        computermove = random.choice(words)
                        print(computermove)
                        print(playerMove)
                        gameResult = gameRules(playerMove, computermove)
                        if gameResult == 'player':
                            player = 1
                            print('You won..')
                        elif gameResult == 'computer':
                            computer = 1
                            print('You lost..')
                        else:
                            print('Draw. Play again.')
            elif userMenuOption == options[1]:
                sys.exit()

if __name__ == '__main__':                 
    main()