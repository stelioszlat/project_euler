from Tools.numbers import number_to_list
from math import pow
from itertools import combinations_with_replacement
# digit fifth powers

numbers = []

# test
powers = []

for i in range(10):
    powers.append(pow(i, 5))

i = 2
while i < 10:
    power_combs = combinations_with_replacement(powers, i)
    for c in power_combs:
        # print(c)
        su = sum(c)
        # print(sum(c))

        s = [int(x) for x in str(int(sum(c)))]
        # print(s)

        # if len(s) == 5:
        number = 0
        for e in s:
            number += pow(e, 5)
        if number == su:
            numbers.append(number)

        # print("-----")
    i += 1

numbers = set(numbers)
print(int(sum(numbers)-1))

# solution: 443839