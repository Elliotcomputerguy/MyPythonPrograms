
def gen_key(server):
    import os, getpass
    serverName = server
    cmdpass = f'ssh-keygen -f id_rsa.{serverName}'
    os.system(cmdpass)

    if os.name == 'nt':
        print('Detected Windows operating system....')
        print('Make directory \.ssh')
        os.system('mkdir C:\Users\username\.ssh')
        username = getpass.getuser()
        os.system(f' id_rsa.{serverName} C:\Users\{username}\.ssh\id_rsa.{serverName}.pub')
        os.system(f' id_rsa.{serverName} C:\Users\{username}\.ssh\id_rsa.{serverName}')
        print('Your public key file and private key file has been copied to c:\users\{username}\.ssh')
        print('Copy your public key to your server to authenticate against using your private key')
    elif os.name == '':
        pass
   # os.system(f'{cmdpass} >> ~/.ssh/authorized_keys')

def main():
    print(''' 
    
    \t\t\t\t Generate a keypair
    
    ''')
    userServer = input('Enter your server name:')
    print('Generating Key......')
    gen_key(userServer)


if __name__ == '__main__':
    main()