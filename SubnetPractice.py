
def internetProtocolAddress():
    ''' Create random ipv4 address'''
    import random
    ipOctetList = []
    for i in range(4):
        octets = random.randrange(1, 255)
        ipOctetList.append(octets)
        while ipOctetList[0] > 223:
            octets = random.randrange(1, 255)
        ipOctetList[0] = octets
        internetProtocolCompleted = ''.join(str(ipOctetList)).replace('[','').replace(']','').replace(',', '.').replace(' ', '')
    return internetProtocolCompleted

def subnetMask():
    ''' Create random subnet mask'''
    import random

    cidr = {
        '/8': '255.0.0.0',
        '/9': '255.128.0.0',
        '/10': '255.192.0.0',
        '/11': '255.224.0.0',
        '/12': '255.240.0.0',
        '/13': '255.248.0.0',
        '/14': '255.252.0.0',
        '/15': '255.254.0.0',
        '/16': '255.255.0.0',
        '/17': '255.255.128.0',
        '/18': '255.255.192.0',
        '/19': '255.255.224.0',
        '/20': '255.255.240.0',
        '/21': '255.255.248.0',
        '/22': '255.255.252.0',
        '/23': '255.255.254.0',
        '/24': '255.255.255.0',
        '/25': '255.255.255.128',
        '/26': '255.255.255.192',
        '/27': '255.255.255.224',
        '/28': '255.255.255.240',
        '/29': '255.255.255.248',
        '/30': '255.255.255.252',
        '/31': '255.255.255.254',
        '/32': '255.255.255.255'
        }
    mask = random.choice(list(cidr.values()))
    return mask

subnetMask()


# print(2 ** 8, 2 ** 7, 2 ** 6, 2 ** 5, 2 ** 4, 2 ** 3, 2 ** 2, 2 ** 1)




    

#    present random ip using range function 1 4,294,967,296 ensuring each octet is below 255 and 223 on the first octet.... 
    
#    ask for network id, broadcast id, subnet mask, how many hosts and how many subnets.

#    create function with formula that gets the network id, broadcast id, sub mask, how many hosts and subnets to th random ip
