
#Create random subnet mask and ipv4 net address
def randomIPandSubnetMask():
    ''' Create random IPV4 network address and subnet mask and return cidr'''
    import random
    
    prefix = 0
    network = 0
    NetworkIdMask = -1
    while NetworkIdMask < 0:

        ipSubnetPrefixList = []

        for i in range(4):
            octets = random.randrange(1, 255)
            ipSubnetPrefixList.append(octets)
            if ipSubnetPrefixList[0] > 223:
                octets = random.randrange(1, 224)
                ipSubnetPrefixList[0] = octets
            
            netAddress = ''.join(str(ipSubnetPrefixList)).replace('[','').replace(']','').replace(',', '.').replace(' ', '')

        cidr = {
            '8': '255.0.0.0',
            '9': '255.128.0.0',
            '10': '255.192.0.0',
            '11': '255.224.0.0',
            '12': '255.240.0.0',
            '13': '255.248.0.0',
            '14': '255.252.0.0',
            '15': '255.254.0.0',
            '16': '255.255.0.0',
            '17': '255.255.128.0',
            '18': '255.255.192.0',
            '19': '255.255.224.0',
            '20': '255.255.240.0',
            '21': '255.255.248.0',
            '22': '255.255.252.0',
            '23': '255.255.254.0',
            '24': '255.255.255.0',
            '25': '255.255.255.128',
            '26': '255.255.255.192',
            '27': '255.255.255.224',
            '28': '255.255.255.240',
            '29': '255.255.255.248',
            '30': '255.255.255.252',
            '31': '255.255.255.254',
            '32': '255.255.255.255'
            }

        randomSubnetMask = random.choice(list(cidr.values()))
        for keyPrefix, subnetMask in cidr.items():
            if subnetMask == randomSubnetMask:
                prefix = int(keyPrefix)
        classRange = ipSubnetPrefixList[0]
        network = int(classRange)
        ipSubnetPrefixList = []

        if network in range(1, 127):
            netClass = 'A'
            n = 8
        elif network in range(128, 193):
            netClass = 'B'
            n = 16
        elif network in range(192, 224):
            netClass = 'C'
            n = 24
        
        NetworkIdMask = prefix - n

    ipSubnetPrefixList.append(netAddress)
    ipSubnetPrefixList.append(randomSubnetMask)
    ipSubnetPrefixList.append(prefix)
    ipSubnetPrefixList.append(netClass)
    return ipSubnetPrefixList

def numberOfSubnets(prefix, IP, classId):
    p = int(prefix)
    if classId == 'A':
        n = 8
    elif classId == 'B':
        n = 16
    elif classId == 'C':
        n = 24
    numOfSubs = p - n
    if numOfSubs <= 0:
        numOfSubsPow = 1
        return numOfSubsPow
    else:
        numOfSubsPow = 2 ** numOfSubs
        return numOfSubsPow

def numberOfHosts(prefix):
    p = int(prefix)
    h = 32
    numOfHosts = h - p
    numOfHostsPow = 2 ** numOfHosts
    return numOfHostsPow 

def main():
    mainList = randomIPandSubnetMask()

    ip = mainList[0]
    print(f'IP address is {ip}')
    subnetmask = mainList[1]
    prefix = mainList[2]
    print(f'subnet mask is {subnetmask} : /{prefix}')
    netClass = mainList[3]
    print(f'network class: {netClass}')
    howManySubs = numberOfSubnets(prefix, ip, netClass)
    print(f'How many subnets: {howManySubs}')
    howmanyHosts = numberOfHosts(prefix)
    print(f'number of hosts: {howmanyHosts}')
main()

#    present random ip using range function 1 4,294,967,296 ensuring each octet is below 255 and 223 on the first octet.... 
    
#    ask for network id, broadcast id, subnet mask, how many hosts and how many subnets.

#    create function with formula that gets the network id, broadcast id, sub mask, how many hosts and subnets




# print(2 ** 8, 2 ** 7, 2 ** 6, 2 ** 5, 2 ** 4, 2 ** 3, 2 ** 2, 2 ** 1)