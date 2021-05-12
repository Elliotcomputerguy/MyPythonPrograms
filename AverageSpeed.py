#!/bin/usr/env python

#accept a number representing the distance;
#accept a number representing the travel time;
#divide the former value by the latter and store the result in the memory;
#display the result (representing the average speed) in a readable format.

def averageSpeed(distance, time):
    try:
        answer = (int(distance) / int(time))
    except ZeroDivisionError:
        return 'You cannot set the divisor to 0!'
    except ValueError:
        return 'You must enter a integer value'
    else:
        return f' Your average speed is {answer} miles per hour'
        
def dist_speed():
    dist = input('Enter your distance in miles:')
    time = input('Enter the travel time in hours:')
    print(averageSpeed(dist, time))
