import pathlib
from datetime import *

class PetRabbit:
    ''' Virtual Pet Rabbit''' #<-- DocString 

    def __init__(self, name): #<-- Constructor method
        self.name = name
        classObjectName = self.name
        classObjectDateOfBirth = str(date.today()).replace('-','')
        pathObject = pathlib.Path.home() / 'PetRabbitConfig.txt'
        if not pathObject.exists():
            pathObject.touch()

            classObjectList = [
                classObjectName,
                classObjectDateOfBirth
                ]

            with pathObject.open(mode='w', encoding='utf-8') as fileObject:
                for items in classObjectList:
                    fileObject.writelines(f'{items}\n')
        elif pathObject.exists():
            classObjectList = []
            with pathObject.open(mode='r', encoding='utf-8') as fileObject:
                for items in fileObject.readlines():
                    fileObjectIndex = items[:-1]
                    classObjectList.append(fileObjectIndex)
            with pathObject.open(mode='a', encoding='utf-8') as fileObject:
                fileObject.writelines(f'{classObjectName}\n')
                fileObject.writelines(f'{classObjectDateOfBirth}\n')

    def classObjectLife(self):
        currentDate = str(date.today()).replace('-','')
        pathObject = pathlib.Path.home() / 'PetRabbitConfig.txt'
        if pathObject.exists():
            classObjectList = []
            with pathObject.open(mode='r', encoding='utf-8') as fileObject:
                for items in fileObject.readlines():
                    fileObjectIndex = items[:-1]
                    classObjectList.append(fileObjectIndex)
            classObjectListLength = len(classObjectList) -1
            print(f'this is the length of the list before loop {classObjectListLength}')
            counter = 0
            counter1 = 0
            for classObjectDate in range(1, classObjectListLength, 2):
                counter1 += 1
                print(f'this is the length of the list in loop {counter} {classObjectListLength}')
                print('this is the list item', counter1, classObjectList[classObjectDate])
                print(int(classObjectList[classObjectDate]) - int(currentDate))

                fileObjectDateOfBirth = int(classObjectList[classObjectDate]) - int(currentDate)

                if fileObjectDateOfBirth >= 30:
                    classObjectDiedDate = classObjectList.pop(classObjectDate)
                    classObjectDiedName = classObjectList.pop(classObjectDate -1)
                    print(f'{classObjectDiedName} passed away and has gone to bunnny heaven. {classObjectDiedName} survived for {fileObjectDateOfBirth} days')
                    #classObjectListLength
                    counter += 1
                    print(f'this is the length of the list after one found {classObjectListLength}')
                    with pathObject.open(mode='w', encoding='utf-8') as fileObject:
                        for items in classObjectList:
                            fileObject.writelines(f'{items}\n')
        return classObjectList


    def enunciate(self, voice): #<-- Object method
        return f'{voice}'

    def __str__(self):          #<-- String method to return name attribute 
        classObject = 'PetRabbit Object\n'
        classObject += f'Name: {self.name}'
        return classObject


rabbit = PetRabbit('jack') #<-- Instantiating an object from the class PetRabbit
#print(rabbit.name)
print(rabbit.classObjectLife())
