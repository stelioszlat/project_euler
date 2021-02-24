
max = 0

for n in range(13, 1000000):
    s = []
    i = n
    while True:

        if i % 2 == 0:
            i /= 2
        else:
            i = 3*i + 1

        s.append(i)

        if i == 1:
            break

    
    if len(s) > max:
        max = n
    


print(max)