import math
from math import sqrt

from Tools.primes import pyth_triples


def iterate_triples():
    r = []
    for i in range(2, 101):
        for j in range(i, 100):
            # for k in range(2, 5):
                t = pyth_triples(i, j)
                print(t)
                if t and t[2] < 1000:
                    r.append(t)
    return r


def filter_tuples(res):
    r1 = []
    r2 = []
    for t in res:
        if t[0] < t[1]:
            r1.append(t)

    for t in r1:
        if t[0] + t[1] + t[2] == 1000:
            r2.append(t)

    return r2


print(filter_tuples(iterate_triples()))
