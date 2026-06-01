
# sum of all positive integers that cannot be written as the sum of two abundant numbers
# upper bound: 28123 (given)

from Tools.numbers import is_abundant, is_perfect

abundants = []

for i in range(1, 28123):
    if is_abundant(i):
        abundants.append(i)

print(abundants)

for i in range(1, 20):
    for a in abundants:
        if i > a:
            break
        else:
            for b in abundants:
                print(a + b)



