
def gen_key(server):
    import os, pathlib, platform

    serverName = server
    cmdpass = f'ssh-keygen -f id_rsa.{serverName}'
    os.system(cmdpass)

    if platform.system() == 'Windows':
        print('Detected Windows operating system....')
    elif platform.system() == 'Linux':
        print('Detected Linux operating system....')

    print('Creating directory \.ssh')

    absPath = pathlib.Path.home() / '.ssh' / 'authorized_keys'
    absPath.mkdir(exist_ok=True)

    os.system(f' move id_rsa.{serverName} {absPath}')
    os.system(f' move id_rsa.{serverName}.pub {absPath}')

    print(f'Your public key file and private key file has been copied to {absPath}')
    print('Copy your public key to your server to authenticate against using your private key')

def main():
    print(''' 
    
    \t\t\t\t Generate a keypair
    
    ''')
    userServer = input('Enter your server name:')
    print('Generating Key......')
    gen_key(userServer)


if __name__ == '__main__':
    main()