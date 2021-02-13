from math import sqrt, floor

x = 600851475143

limit = floor(sqrt(x))

factors = []
prime_factors = []

# find factors
for i in range(1, int(limit)):
    if x % i == 0:
        factors.append(i)

# print(factors)

# remove all even numbers
for i in factors:
    if i % 2 == 0:
        factors.remove(i)

# find prime factors
for i in factors:
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False

    if flag:
        prime_factors.append(i)


# print(prime_factors)

print(prime_factors[-1])

# 6857
