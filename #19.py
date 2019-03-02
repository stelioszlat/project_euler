import calendar as c

months = {'January':31, 'February':28, 'March':31,'April':30,'May':31,
        'June':30, 'July':31, 'August':31, 'September':30, 'October':31,
            'November':30, 'December':31}

lmonths = {'January':31, 'February':29, 'March':31,'April':30,'May':31,
        'June':30, 'July':31, 'August':31, 'September':30, 'October':31,
            'November':30, 'December':31}

week = {1:'Monday', 2:'Tuesday', 3:'Wedsesday', 4:'Thursday',
            5:'Friday', 6:'Saturday', 7:'Sunday'}

sundays = 0
year = 1900
days = 0
last = 0

for i in range(1900, 2001):

    if c.isleap(i):

        for value in lmonths.values():
            for j in range(value):
                days += 1

    else:

        for value in months.values():
            for j in range(value):
                days += 1


print(sundays)
