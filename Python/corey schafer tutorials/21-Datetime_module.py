import datetime as dt
import pytz
"""
Naive datetimes:

-- Less detail, easy to work with
-- Don't have timezones and daylight savings


Aware datetimes: These do have those

first we'll look at naive datetimes
"""
# dt.Date
# only the date
# Create a date (year, month, day)
# Input only integers and do Not add zero
print('---Date---')

d = dt.date(2016, 7, 24)
print(d)

tday = dt.date.today()
print(tday)

print('Year', tday.year)
print('Day', tday.day)
print('Month', tday.month)
print('Weekday', tday.weekday())  # monday 0, sunday 6
print('Isoweekday', tday.isoweekday())  # monday 1, sunday 7

print('\n')

# Time deltas
print('----Time delta----')
tdelta = dt.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

# if we subtract or add a date to a date
bday = dt.date(1998, 5, 16)
my_age = tday - bday
print('You are exactly {} old'.format(my_age))

bday = dt.date(tday.year + 1, 5, 16)
till_bday = bday - tday
print('you have {} until your next bday'.format(till_bday))
print('you have {} days until your next bday'.format(till_bday.days))  # to get just the days
print('you have {:,} seconds until your next bday'.format(till_bday.total_seconds()))

print()
print()

# Dt.time
# only hours
# Hours, minutes, seconds, microseconds
print('----Time----')
t = dt.time(9, 30, 45, 10000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

print()
print()

print('----Datetime----')
# dt.datetime
# date and hours
# Year, month, day, hour, minute, second, microsecond

dtime = dt.datetime(2016, 7, 26, 12, 30, 48, 100000)
print(dtime)
print(dtime.year)
print(dtime.month)
print(dtime.day)
print(dtime.hour)
print(dtime.minute)
print(dtime.second)
print(dtime.microsecond)

print()

tdelta = dt.timedelta(days=7)
print('7 days from dtime is', dtime + tdelta)

print()
print()

# Current time Expressions
print('\n----Current time Expressions----\n')

dt_today = dt.datetime.today()
dt_now = dt.datetime.now()
dt_utcnow = dt.datetime.utcnow()

# These are all the same microseconds are different due to execution times

print('\nThese are all the same microseconds are different due to execution times\n')
print('Today: ', dt_today)
print('Now: ', dt_now)
print('Utcnow: ', dt_utcnow)

'''
today: Current local datetime with a timezone of none
now: Gives the option to give timezone argument, same with today if left empty
utcnow: Current UTC time, timezone is set to none in this example
'''

print()
print()

# For timezone functionality pytz library is recommended by pyhton devs

# pytz recommends always working with UTC
print('----Timezones----\n')
dtime = dt.datetime(2016, 7, 26, 12, 30, 48, 100000, tzinfo=pytz.UTC)
print(dtime)

dt_now = dt.datetime.now(tz=pytz.UTC)  # Preferred method
print('UTC dt.now', dt_now)
dt_utcnow = dt.datetime.utcnow().replace(tzinfo=pytz.UTC)  # Nonsense
print('UTC dt.utcnow', dt_utcnow)

print()

# Converting Timezones
print('----Convert timezones----\n')
dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print('UTC time \t\t\t\t\t ', dt_now)
print('UTC time to Mountain timezone', dt_mtn)

'''
pytz has predifined timezone definitions ('US/Mountain') is one of them
to see all of them you can look at pytz.all_timezones list as below

for tz in pytz.all_timezones:
    print(tz)

'''

print()
print()

# Make a naive datetime into an aware datetime

print('\n Naive datetime into an aware datetime')
dt_naive = dt.datetime.now()

'''
this will give an error because you cant apply timezones to naive datetimes

dt_aware = dt_naive.astimezone(pytz.timezone('US/Eastern'))
'''

# The correct wae :

my_tz = pytz.timezone('US/Mountain')
dt_aware = my_tz.localize(dt_naive)
print('Naive: ', dt_naive)
print('Aware: ', dt_aware)

# Now u know tha wae

print()
print()

print('Displaying datetimes and sharing methods \n')

print('Isoformat: ', dt_aware.isoformat())

# creating a custom format as str with format codes
# docs.python.org/3/library/datetime.html

# strftime: datetime to string
print('\nDatetime as Custom format str: \n', dt_aware.strftime('%B %d, %Y'))

# strptime string do datetime
dt_str = 'July 26, 2016'
dtime = dt.datetime.strptime(dt_str, '%B %d, %Y')

print('\nSTR:', dt_str)
print('Str as Datetime: \n', dtime)
