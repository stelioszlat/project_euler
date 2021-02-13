

f1 = 1
f2 = 1
index = 2

while True:

    f = f1 + f2
    f1 = f2
    f2 = f
    index += 1

    f_listed = [int(x) for x in str(f)]

    if len(f_listed) >= 1000:
        break

print(index)

# solution: 4782