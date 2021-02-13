from math import floor

def is_palindrome(number):
    pass


def is_even(x):
    return True if x % 2 == 0 else False


def is_odd(x):
    return True if x % 2 == 1 else False


def triangular_of(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s


def is_perfect(n, check=False):
    sum = 0

    for d in proper_divisors(n):
        sum += d

    if check:
        return sum
    else:
        if sum == n:
            return True
        return False


def is_deficient(n):
    s = is_perfect(n, True)

    if s < n:
        return True
    return False


def is_abundant(n):
    s = is_perfect(n, True)

    if s > n:
        return True
    return False


def is_divisor(a, b):
    return b % a == 0


def divisors(n):
    for i in range(1, floor(n)+1):
        if is_divisor(i, n):
            yield i

def proper_divisors(n):
    for i in range(1, floor(n/2)+1):
        if is_divisor(i, n):
            yield i

if __name__ == '__main__':
    print(is_abundant(28))
    print(is_perfect(28))
    print(is_deficient(28))
    
