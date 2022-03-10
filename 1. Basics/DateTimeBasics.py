"""
	DATE and TIME
"""


# To work with dates and times, you typically need to use the datetime module.
# Import the datetime module with nickname dt
import datetime as dt


'''
						Working with Dates
'''
# datetime.date : A date consisting of month, day, and year (no time information).
variable = datetime.date(year, month, day)

# Store today's date in a variable named today.
today = dt.date.today()

# Store some other date in a variable called birth_date*
birth_date = dt.date(2019, 12, 31)
print(birth_date.month)
print(birth_date.day)
print(birth_date.year)


'''
						Working with times
'''
# datetime.time : A time consisting of hour, minute, second, microsecond, and optionally time zone information
variable = datetime.time([hour,[minute,[second,[microsecond]]]])
# all the arguments are optional
midnight = dt.time() # 00:00:00
just_morning = dt.time(06,09,00)


'''
						Working with date and time
'''
# datetime.datetime : A single item of data that includes date, time, and optionally time zone information.
variable = datetime.datetime(year, month, day, hour, [minute, [second, [microsecond]]])
# The month, day, and year are required. The rest are optional and set to zero in the time if you omit them.
import datetime as dt
new_years_eve = dt.datetime(2019,12,31,23,59)
print(new_years_eve)


'''
						Formatting Strings for Dates and Times
'''
# %a Weekday, abbreviated Sun
# %A Weekday, full Sunday
# %w Weekday number 0-6, where 0 is Sunday 0
# %d Number day of the month 01-31 31
# %b Month name abbreviated Jan
# %B Month name full January
# %m Month number 01-12 01
# %y Year without century 19
# %Y Year with century 2019
# %H Hour 00-23 23
# %I Hour 00-12 11
# %p AM/PM PM
# %M Minute 00-59 01
# %S Second 00-59 01
# %f Microsecond 000000-999999 495846
# %z UTC offset -0500
# %Z Time zone EST
# %j Day number of year 001-366 300
# %U Week number of year, Sunday as the first day of week, 00-53 50
# %W Week number of year, Monday as the first day of week, 00-53 50
# %c Local version of date and time Tue Dec 31
# 23:59:59 2018
# %x Local version of date 12/31/18
# %X Local version of time 23:59:59
# %% A % character %*

print(f"{birth_date:%A, %B %d, %Y}")
today_s_date = f"{today:%m/%d/%Y}"
print(today_s_date)


'''
						Time Delta
'''
# The timedelta happens automatically when you subtract one date from another to get the time between.
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day

# You can also define any timedelta (duration) using this syntax:
datetime.timedelta(days=, seconds=, microseconds=, milliseconds=, minutes=, hours=, weeks=)

# If you omit an argument, its value is set to zero.
import datetime as dt
new_years_day = dt.date(2019,1,1)
duration = dt.timedelta(days=146)
print(new_years_day + duration) # 2019-05-27

import datetime as dt
now = dt.datetime.now()
birthdatetime = dt.datetime(1995, 3, 31, 8, 26)
age = now - birthdatetime
print(age) # 8634 days, 7:55:07.739804
print(type(age)) # <class 'datetime.timedelta'>




# Example
import datetime as dt

today = dt.date.today()
last_of_teens = dt.date(2019, 12, 31)
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)

print(f"{last_of_teens:%A, %B %d, %Y}")
today_s_date = f"{today:%m/%d/%Y}"
print(today_s_date)
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day
