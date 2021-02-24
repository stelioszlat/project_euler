# Tools for prime numbers
import math
from math import floor, sqrt, pow
from numbers import is_even, is_odd


def is_prime(number):
    pass



def primes_until(number):
    nums = []
    for i in range(2, number):
        nums.append(i)
    p = 2
    point = 0
    while True:
        for i in range(2*p, nums.__len__()+1, p):
            nums.remove(i)

        point += 1
        p = nums[point]
        if p == nums[-1]:
            break

    return nums



def prime_factors(number):
    pass


def are_co_prime(p, q):
    return True if math.gcd(p, q) == 1 else False


def pyth_triples(n, m, k=1):
    """
    given n and m, returns a tuple of the pythagorean triple
    based on Euclid's formula
    :param n: positive integer
    :param m: positive integer
    :param k: parameter
    :return: tuple of three integers
    """
    if n < 0 or m < 0:
        print("m or n negative...try again")
        return

    if are_co_prime(n, m):
        if m > n:
            if not(is_odd(n) and is_odd(n)):
                a = k * (pow(m, 2) - pow(n, 2))
                b = k * (2 * m * n)
                c = k * (pow(m, 2) + pow(n, 2))
                t = (a, b, c)
                return t
            # else:
                # print("both m and n are even")
                # return
        else:
            # print("m is not larger than n")
            return
    else:
        # print("n and m are not co-prime")
        return


if __name__ == '__main__':

    print(pyth_triples(3, 6))

# even and odd = True
# even and even = False
# odd and odd = False
# odd and even = True

# not even xor not even
# False xor True = True
# False xor False = False
# True xor True = False
# True xor False = True