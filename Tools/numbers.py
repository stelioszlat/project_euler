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
    divs = []
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            divs.append(i)

    for d in divs:
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


def are_amicable(a, b):
    if a != b:
        return sum_divisors(a) == b and sum_divisors(b) == a


def is_divisor(a, b):
    return b % a == 0


def divisors(n):
    for i in range(1, floor(n)+1):
        if is_divisor(i, n):
            yield i


def sum_divisors(n):
    return sum(divisors(n))

if __name__ == '__main__':
    for i in range(1, floor(28)+1):
        if(is_divisor(i, 28)):
            print(str(i))
