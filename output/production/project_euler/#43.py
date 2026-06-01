
combs = []


def combinations(number, cur, n):

    number[0] = cur

    for i in range(n):

        if i != cur:
            number = combinations(number, i, n - 1)

        if n == 1:
            number[-1] = i
            return number



# for i in range(10):
#
#     temp = []
#
#     for j in range(10):
#         temp.append(-1)
#
#     for j in range(j):
#         temp[j] = (i + j) % 10
#
#     print(temp)

for i in range(10):
    combs.append(-1)

combinations(combs, 0, 10)
