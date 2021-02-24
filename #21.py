
from Tools.numbers import sum_divisors

sum = 0

# if d(a) == b and d(b) == a: a and b are amicable
# find the sum of all amicable numbers under 10.000

for i in range(1, 10000):
    a = sum_divisors(i)
    if sum_divisors(a) == i:
        sum += a + i


print(sum)