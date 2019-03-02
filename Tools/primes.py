# Tools for prime numbers
import math
from math import floor, sqrt

def is_prime(number):
    flag = True
    for j in range(2, number):
        if number % j == 0:
            flag = False

    if flag:
        return True
    return False


def primes_until(number):

    list = []
    primes = []

    for i in range(2, number):
        list.append(i)

    for i in list:
        if is_prime(i):
            primes.append(i)

        # print(str(i*100/number) + "%") # percentage status

    return primes


def prime_factors(number):
    pass


if __name__ == '__main__':
    print(primes_until(20))
