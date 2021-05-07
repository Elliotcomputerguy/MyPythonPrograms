
import pathlib
from pathlib import Path

basalt, breccia, highland, regolith = 0, 0, 0, 0

print('Artemis Rover Rock Scanner Starting')
strPath = pathlib.Path('C:/Users/ElliotStenning/Documents/Python/rocks.txt')

with strPath.open(mode = 'r', encoding='utf-8') as fileObject:
    rockList = [line.rstrip() for line in fileObject.readlines()]

def countMoonRocks(rockToID):
    print(rockToID)
    if rockToID in rockList:
        if rockToID == rockList[0]:
            global basalt
            basalt += 1
        elif rockToID == rockList[1]:
            global breccia
            breccia += 1
        elif rockToID == rockList[2]:
            global highland
            highland += 1
        elif rockToID == rockList[3]:
            global regolith
            regolith += 1            
        return

for rock in rockList:
    countMoonRocks(rock)
    
print(f'''
    ##############################
    Number of Basalt:   {basalt}
    Number of Breccia:  {breccia}
    Number of Highland: {highland}
    Number of Regolith: {regolith}
    ##############################
''')
print('The max number of one type of rock found was:', max(basalt, breccia, highland,regolith))
print('The minimum number of one type of rock found was:', min(basalt, breccia, highland, regolith))