
def let(l):
    sum = 0
    for word in l:
        print(word)
        for let in word:
            if let != ' ':
                sum += 1
    return sum

one_to_nine = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_nineteen = ['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen']

dec = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
hundred = 'hundred'
thaousand = 'one thousand'

all = []
new_str = ''

for t in one_to_nine:
    all.append(t)
for t in ten_to_nineteen:
    all.append(t)

for d in dec:
    all.append(d)
    for o in one_to_nine:
        new_str = d + ' ' + o
        all.append(new_str)

for o in one_to_nine:
    all.append(o + ' ' + hundred)
    new_hs = o + ' ' + hundred + ' and '
    for t in one_to_nine:
        all.append(new_hs + ' ' + t)
    for t in ten_to_nineteen:
        all.append(new_hs + ' ' + t)

    for d in dec:
        all.append(new_hs + ' ' + d)
        for t in one_to_nine:
            new_str = new_hs + d + ' ' + t
            all.append(new_str)

all.append(thaousand)

print(all)
total = let(all)
print(total)

# answer: 21124
