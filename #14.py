
max = 0

for n in range(13, 1000001):
    count = 0
    i = n
    while True:

        if i % 2 == 0:
            i /= 2
        else:
            i = 3*i + 1

        count += 1

        if i == 1:
            count += 1
            break

    if count > max:
        max = n


print(max)