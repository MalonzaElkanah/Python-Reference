# Import the datetime module, nickname dt
import datetime as dt
# Store today's date in a variable named today.
today = dt.date.today()
# Store some other date in a variable called last_of_teens
last_of_teens = dt.date(2019, 12, 31)
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)
# Formatting Strings for Dates and Times

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
# %% A % character %

print(f"{last_of_teens:%A, %B %d, %Y}")
today_s_date = f"{today:%m/%d/%Y}"
print(today_s_date)
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day
