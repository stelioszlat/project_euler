num = []
n = 0
while len(num) < 1000001:
    str_num = [int(x) for x in str(n)]
    num += str_num
    n += 1

mul = num[1] * num[10] * num[100] * num[1000] * num[10000] * num[100000] * num[1000000]
print(mul)

# answer: 210