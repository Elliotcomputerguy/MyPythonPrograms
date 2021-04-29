#!/usr/bin/env python
import datetime
 
dt = datetime.datetime.today()
userDob = input('Please enter your date of Birth in DD-MM-YYYY:')
for i in userDob:
    if '0' in userDob:
        userDob = userDob.replace('0','a')
if 'a' not in userDob:
    userDay = userDob[0:2] 
    userMonth = userDob[2:4]
    userYear = userDob[4:]

elif userDob[0:1] == 'a' and userDob[2:3] == 'a':
    userDob = userDob.replace('a', '')
    userDay = userDob[0:1]
    userMonth = userDob[2:3]
    userYear = userDob[2:]

elif userDob[0:1] == 'a' and userDob[3:4] =='a':
    userDob = userDob.replace('a', '')
    userDay = userDob[0:1]
    userMonth = userDob[3:4]
    userYear = userDob[2:]

elif userDob[0:1] == 'a':
    userDob = userDob.replace('a', '')
    userDay = userDob[0:1]
    userMonth = userDob[2:4]
    userYear = userDob[3:] 

currentAge  = int(dt.day) - int(userDay) and int(dt.month) - int(userMonth) and int(dt.year) - int(userYear)
futureYear = int(dt.year) + 10
print('Your age is ' + str(currentAge) + '\nYou will be ' + str(int(currentAge) + int(10)) + ', 10 years from now in the year ' + str(futureYear))
