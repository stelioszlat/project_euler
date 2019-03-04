import math
from math import sqrt

powers = []
sums = []
sqrts = []

for a in range(1, 1000):

    powers.append(a ** 2)

print(powers)

for i in powers:
    for j in powers:
        sums.append(i + j)

print(sums)

for i in sums:
    s = sqrt(i)
    if s < 1000:
        if not isinstance(s, float):
            sqrts.append(s)

print(sqrts)


# ================================================ #
# old version
# summary = 0
# list1 = [
#     [],  # holds a values
#     [],  # holds b values
#     [],  # holds c values
# ]
#
# flag = True
# a = 1
# b = 1
# c = 1
# pa = 0
# pb = 0
# pc = 0
# while flag:
#
#     summary = 0
#     c_pwer = c ** 2
#
#     for a in range(c_pwer):
#         for b in range(c_pwer):
#             a_pwer = a ** 2
#             b_pwer = b ** 2
#
#             if a_pwer + b_pwer == c_pwer:
#                 list1[0].append(a)
#                 list1[1].append(b)
#                 list1[2].append(c)
#
#     print(list1)
#
#     c += 1
#
#     for i in range(list1[1].__len__()):
#         summary = list1[0][i] + list1[1][i] + list1[2][i]
#         if summary == 1000:
#             flag = False
#             pa = list1[0][i]
#             pb = list1[1][i]
#             pc = list1[2][i]
#
# product = pa * pb * pc
#
# print(product)
