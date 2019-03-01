
from Tools.factors import *
from Tools.triang_numbers import get_triang_number

num = 29 # don't have to check for 28 or less
while True:
    trian = get_triang_number(num)
    f = factors(trian)

    print(trian)
    print(len(f))
    print(f)
    if len(f) > 100 :
        break
    num += 1

print(trian)
