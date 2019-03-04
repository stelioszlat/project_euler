from Tools.primes import primes_until


primes = primes_until(2000000)

sum = 0

for p in primes:
    # print(str(p / len(primes) * 100) + "%")
    print(str(sum))
    sum += int(p)

print(sum)
