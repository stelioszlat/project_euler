import math
from math import sqrt

from Tools.primes import pyth_triples




for i in range(2, 1001):
    for j in range(2, 1001):
        
        t = pyth_triples(i, j)
        print(t)
        if t and t[1] + t[2] + t[3] == 1000:
            print(t)





