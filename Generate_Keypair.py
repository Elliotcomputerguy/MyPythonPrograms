
def get_admin():
    import os, ctypes
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin


def gen_key(server,username,privatekey):
    import os, pathlib, platform, time, sys

    serverName = server
    userName = username
    privateKey = privatekey
    
    if platform.system() == 'Windows':
        print('Detected Windows operating system....')
        isadmin = get_admin()
        if isadmin == 'False':
            print('This needs to be ran as Administrator...')
            time.sleep(5)
            sys.exit()
        else:
            os.system('Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0')
            os.system('move C:\Windows\System32\OpenSSH\*.exe c:\Windows\System32')
            
    elif platform.system() == 'Linux':
        print('Detected Linux operating system....')

    absPath = pathlib.Path.home() / '.ssh' / 'authorized_keys'
    absPath.mkdir(exist_ok=True)
   # sshPath = pathlib.Path.home() / '.ssh' 

    cmdpass = f'ssh-keygen -t rsa -m PEM -b 4096 -C {userName}@{serverName} -f {absPath}/{privateKey}'
    os.system(cmdpass)

    print(f'Your public key file and private key file has been copied to {absPath}')
    print('Copy your public key to your server to authenticate against using your private key')

def main():
    print(''' 
    
    \t\t\t\t Generate a keypair
    
    ''')
    userServer = input('Enter your server name:')
    userName = input('Enter your username:')
    privateKey = input('Enter a private key file name:')
    print('Generating Key......')
    gen_key(userServer,userName,privateKey)

if __name__ == '__main__':
    main()