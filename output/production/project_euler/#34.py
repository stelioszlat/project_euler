
from Tools.factors import factorial

n = 10
total = 0
while n < 10000000:

    digits = [int(x) for x in str(n)]
    sum = 0
    for d in digits:
        sum += factorial(d)

    if sum == n:
        total += n

    n += 1

print(total)