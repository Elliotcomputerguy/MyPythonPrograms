import time
# Azure function to create a vm
def az_vm():
    az = 'azvm'
    print(az)
    var = input('>')
    time.sleep(6)
    return '-----------'

# module dictionary
def moduleLibrary(arg=''):

    moduleLibrary = {
    'az_vm':'Create a Azure vm : Mod ver 0.1 2021 TF Ver 15',
    'aws_instance':'Create a AWS instance : Mod ver 0.1 2021 TF Ver 15',
    }
    if arg:
        if arg in moduleLibrary:
            try:
                if arg == 'az_vm':
                    az_vm()
                elif arg == 'aws_instance':
                    aws_vm()
            except TypeError:
                print('Error')
                time.sleep(6)
        else:
            print(f'{arg} module not in library')
            time.sleep(6)
    else:
        for module in moduleLibrary:
            moduleLib = f'{module} : {moduleLibrary[module]}'
            print(moduleLib)
        return '------------------------------------------------------'


# AWS function to create an instance
def aws_vm():
    aws = 'awsvm'
    print(aws)
    var = input('>')
    time.sleep(6)
    return '----------'

# help
def help():
    import time
    print('''

           cmds:...........................
           --------------------------------
           showLib to browse Modules                    
           <module-name> to load                 
           exit
           mkdir
           terraform init
           terraform plan
           terraform apply                                 
           --------------------------------                                              
        
    ''')
    time.sleep(6)



# main
def main():
    import sys, os, time
    while True:
        os.system('cls')
        print('''
                                           -
                                          -----                           -
                                          ---------                      --
                                          ---------  -                -----
                                           ---------  ------        -------
                                             -------  ---------  ----------
                                                ----  ---------- ----------
                                                  --  ---------- ----------
   Welcome to Terraform Automation Modules         -  ---------- -------
                                                      ---  ----- ---
   Documentation: ElliotComputerguy.com               --------   -
                                                      ----------
                                                      ----------
                                                       ---------
                                                           -----
                                                               -

        ''')

        userInput = input('>').lower().strip()
        if userInput == 'help':
            help()
        elif userInput == 'exit':
            sys.exit()
        elif userInput == 'showlib':
            print(moduleLibrary())
            time.sleep(6)
        else:
            print(moduleLibrary(userInput))

main()