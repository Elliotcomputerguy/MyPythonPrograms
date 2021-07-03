
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
    pass



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
                    playerMove = input('Enter Rock Paper or Sicssors >')
                    if playerMove == 'e' or playerMove == 'E':
                        sys.exit()
                    else:
                        computermove = random.choice(words)
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