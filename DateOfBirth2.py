import datetime, math
dt = datetime.datetime.today()
userDob = input('Please enter your date of Birth in DD-MM-YYYY:') 
if '0' in userDob:
    userDob = userDob.replace('0','.0')
    userDay = userDob[0:3] 
    userMonth = userDob[3:6]
    userYear = userDob[6:]
    currentAge  = float(dt.day) - float(userDay) and float(dt.month) - float(userMonth) and int(dt.year) - int(userYear)
else:
    userDay = userDob[0:2] 
    userMonth = userDob[2:4]
    userYear = userDob[4:]
    currentAge  = int(dt.day) - int(userDay) and int(dt.month) - int(userMonth) and int(dt.year) - int(userYear)


futureYear = int(dt.year) + 10
print('Your age is ' + str(currentAge) + '\nYou will be ' + str(int(currentAge) + int(10)) + ', 10 years from now in the year ' + str(futureYear))