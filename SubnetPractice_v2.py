# have not add private address rule for 172.16.0.0 - 172.31.255.255 /12
# ...program title...
def main_title():
    ''' Title'''
    title =  print('''
10101010 00101010 01110101 01010110 10101010 11010101 10101010 00101010 01110101 01010110 10101010 11010101 10101010 00101010 01110101 01010110 101
███████╗██╗   ██╗██████╗ ███╗   ██╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗     ██████╗ ██████╗  █████╗  ██████╗████████╗██╗ ██████╗███████╗
██╔════╝██║   ██║██╔══██╗████╗  ██║██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║██╔════╝██╔════╝
███████╗██║   ██║██████╔╝██╔██╗ ██║█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗    ██████╔╝██████╔╝███████║██║        ██║   ██║██║     █████╗  
╚════██║██║   ██║██╔══██╗██║╚██╗██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║    ██╔═══╝ ██╔══██╗██╔══██║██║        ██║   ██║██║     ██╔══╝  
███████║╚██████╔╝██████╔╝██║ ╚████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝    ██║     ██║  ██║██║  ██║╚██████╗   ██║   ██║╚██████╗███████╗
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝
10101010 00101010 01110101 01010110 10101010 11010101 10101010 00101010 01110101 01010110 10101010 11010101 10101010 00101010 01110101 01010110 101
    ''')
    return title

# ...Check that ipcalc is installed. If not install using pip...
def setup():
    ''' install ipcalc module if not installed'''
    import os
    package = "ipcalc"
    try:
        __import__(package)
    except:
        os.system("pip install "+ package)

# ...Create random ipv4 address...
def createRandInternetProtocolAddress():
    ''' Create random ipv4 address'''
    import random
    ipoctetList = []
    for _ in range(4):
        octets = random.randrange(1, 255)
        ipoctetList.append(octets)
    if ipoctetList[0] > 223:
        octets = random.randrange(1, 224)
        ipoctetList[0] = octets
    internetProtocolv4 = ''.join(str(ipoctetList)).replace('[','').replace(']','').replace(',', '.').replace(' ', '')

    return internetProtocolv4

# ...Create random netmask with prefix...
def randNetMask():
    import random
    ipSubnetPrefixList = []
    cidr = {
            '8': '255.0.0.0', '9': '255.128.0.0', '10': '255.192.0.0', '11': '255.224.0.0', '12': '255.240.0.0', '13': '255.248.0.0',
            '14': '255.252.0.0', '15': '255.254.0.0', '16': '255.255.0.0', '17': '255.255.128.0', '18': '255.255.192.0', '19': '255.255.224.0',
            '20': '255.255.240.0', '21': '255.255.248.0', '22': '255.255.252.0', '23': '255.255.254.0', '24': '255.255.255.0', '25': '255.255.255.128',
            '26': '255.255.255.192', '27': '255.255.255.224', '28': '255.255.255.240', '29': '255.255.255.248', '30': '255.255.255.252', '31': '255.255.255.254',
            '32': '255.255.255.255'
    }

    randomSubnetMask = random.choice(list(cidr.values()))
    for keyPrefix, subnetMask in cidr.items():
        if subnetMask == randomSubnetMask:
            prefix = int(keyPrefix)
            ipSubnetPrefixList.append(prefix)
            ipSubnetPrefixList.append(randomSubnetMask)
    return ipSubnetPrefixList

def netclass_a_b_c(netclasscheck):

    netclasslist = netclasscheck.split('.')
    octet = int(netclasslist[0])

    if octet < 126:
        netclass = 'A' 
    elif octet < 191:
        netclass = 'B'
    elif octet < 223:
        netclass = 'C'
    return netclass

def netwrapup():

    netlist = []
    netaddress = createRandInternetProtocolAddress()
    netmasklist = randNetMask()
    prefix = netmasklist.pop(0)
    netmask = netmasklist.pop(0)
    netclass = netclass_a_b_c(netaddress)
    netlist.append(netaddress)
    netlist.append(prefix)
    netlist.append(netmask)
    netlist.append(netclass)
    return netlist

def netrules():
    netlist = netwrapup()

    while netlist[3] == 'B' and netlist[1] < 16:
        netlist = netwrapup()
    while netlist[3] == 'C' and netlist[1] < 24:
        netlist = netwrapup()

    return netlist

# ...Using tehmaze ipcalc to return first host, last host, broadcast, how many hosts, prefix, netmask. 
# ...ipcalc can be found at https://pypi.org/project/ipcalc/#files
# ...https://github.com/tehmaze/ipcalc

def ipcalcFunc(ip, prefix):
    import ipcalc
    ipcalcList = []
    net = str(f'{ip}/{prefix}')
    net = ipcalc.Network(net)
    ipcalcList.append(net.broadcast())
    ipcalcList.append(net.host_first())
    ipcalcList.append(net.host_last())
    ipcalcList.append(net.size())
    ipcalcList.append(net.network())
    return ipcalcList

def main():
    import sys, os, time
    setup()
    while True:
        os.system('cls')
        unpacklist = netrules()
        netaddress, prefix, netmask, netclass = unpacklist
        ipcalclist = ipcalcFunc(netaddress, prefix)
        joinipcalc = ''.join(str(ipcalclist).replace('IP','').replace('(','').replace(')','').replace('[','').replace(']','').replace("'",""))
        ipcalclist = joinipcalc.split(',')
        options = (1,2)
        broadcast, firstip, lastip, hosts, netid = ipcalclist
        hosts = int(hosts)
        hosts = hosts - 2
        option = ''
        main_title()
        print('''
                                                \t[1] Subnet practice    
                                                \t[2] Exit                 
        ''')
        while option not in options:
            try:
                option = int(input('Option >'))
            except ValueError:
                print('Invalid option input')

        if option == options[0]:
            print(f'\nip address : {netaddress}')
            print(f'subnet mask :{netmask} and prefix : /{prefix}')
            print(f'IP class : {netclass}')
            print(f'network id : {netid}')
            print(f'First ip address : {firstip}')
            print(f'Last ip address : {lastip}')
            print(f'Broadcast address : {broadcast}')
            print(f'How many hosts : {hosts}\n')
            time.sleep(6)
        elif option == options[1]:
            sys.exit()
    
if __name__ == '__main__':
    main()



    









