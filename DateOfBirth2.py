import datetime

def dateOfBirth(date):
    currentDate = datetime.datetime.today()
    if '0' in date:
        date = date.replace('0','.0')
        dateDay = date[0:3]
        dateMonth = date[3:6]
        dateYear = date[6:]
        currentAge = float(currentDate.day) - float(dateDay) and float(currentDate.month) - float(dateMonth) and int(currentDate.year) - int(dateYear)
        return currentAge
    else:
        dateDay = date[0:2]
        dateMonth = date[2:4]
        dateYear = date[4:]
        currentAge = int(currentDate.day) - int(dateDay) and int(currentDate.month) - int(dateMonth) and int(currentDate.year) - int(dateYear)
        return currentAge

def main():
    dob = input('Please enter your date of Birth in DD-MM-YYYY:')
    futureYear = int(dt.year) + 10
    print('Your age is ' + str(currentAge) + '\nYou will be ' + str(int(currentAge) + int(10)) + ', 10 years from now in the year ' + str(futureYear))



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