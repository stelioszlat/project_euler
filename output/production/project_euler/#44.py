
# Pn = n(3n - 1)/2
import math

pentagonal = []
min = 1
max = 10000
d = 0
while True:
    for i in range(min, max):
        pentagonal.append(int(i*(3*i - 1)/2))

    d = pentagonal[min]

    for i in pentagonal:
        for j in pentagonal:
            if i == j:
                continue
            cur = math.fabs(i - j)
            if cur < d:
                d = cur
                print(d)

