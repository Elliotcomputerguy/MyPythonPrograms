import sys, os, time

# How old are in seconds ? 
# There are 365 days in the year, 24 hours in the day, 60 minutes in a hour and 60 seconds in a minute. 

def main():

    while True:
        os.system('cls')
        print('''

 ('-. .-.               (`\ .-') /`                             _ .-') _           ('-.     _  .-')     ('-.                                                    
( OO )  /                `.( OO ),'                            ( (  OO) )         ( OO ).-.( \( -O )  _(  OO)                                                   
,--. ,--. .-'),-----. ,--./  .--.         .-'),-----.  ,--.     \     .'_         / . --. / ,------. (,------.        ,--.   ,--..-'),-----.  ,--. ,--.         
|  | |  |( OO'  .-.  '|      |  |        ( OO'  .-.  ' |  |.-') ,`'--   _)        | \-.  \  |   /`. ' |  .---'         \  `.'  /( OO'  .-.  ' |  | |  |         
|   .|  |/   |  | |  ||  |   |  |,       /   |  | |  | |  | OO )|  |  \  '      .-'-'  |  | |  /  | | |  |           .-')     / /   |  | |  | |  | | .-')       
|       |\_) |  |\|  ||  |.'.|  |_)      \_) |  |\|  | |  |`-' ||  |   ' |       \| |_.'  | |  |_.' |(|  '--.       (OO  \   /  \_) |  |\|  | |  |_|( OO )      
|  .-.  |  \ |  | |  ||         |          \ |  | |  |(|  '---.'|  |   / :        |  .-.  | |  .  '.' |  .--'        |   /  /\_   \ |  | |  | |  | | `-' /      
|  | |  |   `'  '-'  '|   ,'.   |           `'  '-'  ' |      | |  '--'  /        |  | |  | |  |\  \  |  `---.       `-./  /.__)   `'  '-'  '('  '-'(_.-'       
`--' `--'     `-----' '--'   '--'             `-----'  `------' `-------'         `--' `--' `--' '--' `------'         `--'          `-----'   `-----'          
                                                              .-') _         .-')      ('-.                               .-') _  _ .-') _    .-')              
                                                             ( OO ) )       ( OO ).  _(  OO)                             ( OO ) )( (  OO) )  ( OO ).            
                                                  ,-.-') ,--./ ,--,'       (_)---\_)(,------.   .-----.  .-'),-----. ,--./ ,--,'  \     .'_ (_)---\_)           
                                                  |  |OO)|   \ |  |\       /    _ |  |  .---'  '  .--./ ( OO'  .-.  '|   \ |  |\  ,`'--   _)/    _ |            
                                                  |  |  \|    \|  | )      \  :` `.  |  |      |  |('-. /   |  | |  ||    \|  | ) |  |  \  '\  :` `.            
                                                  |  |(_/|  .     |/        '..`''.)(|  '--.  /_) |OO  )\_) |  |\|  ||  .     |/  |  |   ' | '..`''.)           
                                                 ,|  |_.'|  |\    |        .-._)   \ |  .--'  ||  |`-'|   \ |  | |  ||  |\    |   |  |   / :.-._)   \           
                                                (_|  |   |  | \   |        \       / |  `---.(_'  '--'\    `'  '-'  '|  | \   |   |  '--'  /\       /           
                                                  `--'   `--'  `--'         `-----'  `------'   `-----'      `-----' `--'  `--'   `-------'  `-----'  
''')
        print('\t\ttype exit to leave the program')
        yourAge = input('\t\tWhat is your age:')
        yourAgeExit = yourAge.upper()
        if yourAgeExit == 'EXIT':
            sys.exit()
        else:
            yourAge = int(yourAge)
            seconds = yourAge * 365 * 24 * 60 * 60
            if seconds >= 1576800000:
                print('\t\tYou are this old in seconds %s. That is really old!' % seconds)
                time.sleep(6)   # Delays for 5 seconds.
            else:
                print('\t\tYou are this old in seconds %s. Your not that old yet!' % seconds)
                time.sleep(6)   # Delays for 5 seconds.

main()
