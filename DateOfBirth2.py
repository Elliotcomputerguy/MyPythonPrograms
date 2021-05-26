import datetime

def currentdate():
    currentDateYear = datetime.datetime.today().year
    return currentDateYear

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
    dob = ''
    while not dob:
        dob = input('Please enter your date of Birth in DD-MM-YYYY:')

    if len(dob) == 8 and dob.isdigit:
        try:
            currentAge = dateOfBirth(dob)
            futureYear = int(currentdate()) + 10
        except TypeError:
            print('Enter a number')
        print('Your age is ' + str(currentAge) + '\nYou will be ' + str(int(currentAge) + int(10)) + ', 10 years from now in the year ' + str(futureYear))
    else:
        if len(dob) == 10 and '/' in dob:
            dob = dob.replace('/','')
            try:
                currentAge = dateOfBirth(dob)
                futureYear = int(currentdate()) + 10
            except TypeError:
                print('Enter a number')
            print('Your age is ' + str(currentAge) + '\nYou will be ' + str(int(currentAge) + int(10)) + ', 10 years from now in the year ' + str(futureYear))
        elif len(dob) == 10 and '-' in dob:
            dob = dob.replace('-','')
            try:
                currentAge = dateOfBirth(dob)
                futureYear = int(currentdate()) + 10
            except TypeError:
                print('Enter a number')
            print('Your age is ' + str(currentAge) + '\nYou will be ' + str(int(currentAge) + int(10)) + ', 10 years from now in the year ' + str(futureYear))
        else:
            print('error')


main()