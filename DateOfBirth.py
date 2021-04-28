#!/usr/bin/env python

from datetime import date

import datetime
year = datetime.date.today().year

userDob = input('Please enter your date of birth:')
currentAge = str(int(year) - int(userDob))
futureYear = str(int(year + 10))
print(futureYear)
print('Your age is ' + str(currentAge) + '\nYou will be ' + str(int(futureYear) - int(userDob)) + ', 10 years from now in the year ' + str(futureYear))
