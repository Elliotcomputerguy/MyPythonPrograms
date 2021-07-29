def gen_key(server):
    import os
    serverName = server
    cmdpass = f'ssh-keygen -f id_rsa.{serverName}'
    os.system(cmdpass)
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