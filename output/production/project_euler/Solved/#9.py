import math
from math import sqrt

def pyth_triples():
    for i in range(2, 1000):
        for j in range(2, 1000):
            if i + j + sqrt(i**2+j**2) == 1000:
                print(int(i * j * sqrt(i**2 + j**2)))
                return

pyth_triples()