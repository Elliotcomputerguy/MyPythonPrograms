import sys

# How old are in seconds ? 
# There are 365 days in the year, 24 hours in the day, 60 minutes in a hour and 60 seconds in a minute. 

def main():

    while True:
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
        print('type exit to leave the program')
        yourAge = input('What is your age:')
        yourAgeExit = yourAge.upper()
        if yourAgeExit == 'EXIT':
            sys.exit()
        else:
            yourAge = int(yourAge)
            seconds = yourAge * 365 * 24 * 60 * 60
            print('You are %s old in seconds!' % seconds)
main()