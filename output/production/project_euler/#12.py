
# from Tools.factors import *
from Tools.numbers import triangular_of, divisors

n = 1000                    #  divs > floor(triang / 2) => (floor(triang / 2) < triang) 2 * divs > triang
flag = True
last = triangular_of(999)           # triang(x) = triang(x - 1) + x

while flag:

    triang = last + n
    count = 0
    for i in divisors(triang):
        if count >= 500:
            print(triang)
            flag = False
            break
        count += 1
    n += 1