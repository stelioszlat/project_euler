from Tools import primes

count = 0
i = 2
while count < 10001:
    p = primes.is_prime(i)

    print(p)
    if p:
        count += 1
        print(str(i) + ':' + str(count))
    i += 1

print(count)

p = primes.is_prime(i)
print(p)

# result : 104743