from Tools.progress import Main

sequences = {}

# m = Main()
for n in range(13, 1000001):
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

    # print(s)

    # m.progress(round(n/1000001))
    sequences[n] = s

print(sequences)

s = sequences.values()
lens = []

for i in s:
    lens.append(len(i))

mx = max(lens)
mx_index = lens.index(mx) + 13

print(mx)
print(mx_index)