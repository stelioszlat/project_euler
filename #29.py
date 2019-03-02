
combinations = []

for i in range(2, 100):
    for j in range(2, 100):
        combinations.append(i**2)

c = set(combinations)

print(c)
