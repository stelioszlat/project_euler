

def factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors



if __name__ == '__main__':
    nums = [1, 3, 6, 10, 15, 21, 28]
    for i in nums:
        print(factors(i))
