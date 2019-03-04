# Tools for prime numbers
import math
from math import floor, sqrt

def is_prime(number):
    flag = True
    for j in range(2, floor(sqrt(number))):
        if number % j == 0:
            flag = False

    if flag:
        return True
    return False


def primes_until(number, file=False):

    primes = []

    if file:
        with open('C:\\users\\zlat\\Documents\\projecteuler\\primes.txt', 'r') as f:
            primes = f.readlines()
        return primes
    else:
        f = open("primes.txt", 'w')
        f.write(str(number) + '\n')

        for i in range(2, number):
            if is_prime(i):
                primes.append(i)
                f.write(str(i))

            print(str(i*100/number) + "%") # percentage status

        f.close()
        return primes


def prime_factors(number):
    pass


if __name__ == '__main__':
    print(primes_until(20))
