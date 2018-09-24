from Tools.primes import primes_until


primes = primes_until(2000000)

sum = 0

for p in primes:
    # print(p)
    sum += p

print(sum)