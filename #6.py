sum1 = 0
sum2 = 0

for i in range(1, 101):
    sum1 += i * i
    sum2 += i

sum2 *= sum2

# print(sum1)
# print(sum2)
print(sum2 - sum1)

#  result : 25164150