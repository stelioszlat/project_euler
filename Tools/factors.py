

def factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    nums = [1, 3, 6, 10, 15, 21, 28]
    for i in nums:
        print(factors(i))

    # print(factorial(15))
