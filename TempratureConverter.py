#!/usr/bin/env python

def convert_cel_to_far(c):
    f = c * 9/5 + 32
    return float(f)

userCelciusConvert = int(input('Enter a Celsius temprature to convert to Farneheit:'))
print(convert_cel_to_far(userCelciusConvert))

def convert_far_to_cel(f):
    c = (f - 32) * 5/9
    return float(c)

userFarneheitConvert = int(input('Enter a Farenheit temprature to convert to Celsius:'))
print(convert_far_to_cel(userFarneheitConvert))