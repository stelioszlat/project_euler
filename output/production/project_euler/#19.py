
from Tools.time import is_leap
from itertools import cycle

nmonths = {'January':31, 'February':28, 'March':31,'April':30,'May':31,
        'June':30, 'July':31, 'August':31, 'September':30, 'October':31,
            'November':30, 'December':31}

lmonths = {'January':31, 'February':29, 'March':31,'April':30,'May':31,
        'June':30, 'July':31, 'August':31, 'September':30, 'October':31,
            'November':30, 'December':31}

week = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday',
            5:'Friday', 6:'Saturday', 7:'Sunday'}

days_count = 0
sundays = 0
year_changes = 0
month_changes = 0
week_changes = 0

#  1 Jan 1900 was Monday
#

#  start on 1st January 1901, end on 31st December 2000
year = 1900
week_iter = cycle(week)         # use cyclic iteration for week day
day = 0
# calculate first day
months = nmonths
for month in months.values():
    for i in range(month):
        day = next(week_iter)

year += 1

while year_changes < 100:

    if is_leap(year):
        # use lmonths
        months = lmonths
    else:
        # use months
        months = nmonths

    for month in months.values():
        for i in range(month):
            if week.get(day) == 'Sunday':
                sundays += 1
                week_changes += 1
            days_count += 1
            day = next(week_iter)       # get next day
        month_changes += 1

    year_changes += 1
    year += 1




print('Total days:\t\t\t\t'+str(days_count)
      +'\nTotal years:\t\t\t'+str(year_changes)
      +'\nTotal months:\t\t\t'+str(month_changes)
      +'\nTotal weeks:\t\t\t'+str(week_changes)
      +'\n\nSundays:\t\t\t\t'+str(sundays))



