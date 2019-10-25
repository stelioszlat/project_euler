
combinations = []

for i in range(2, 101):
    for j in range(2, 101):
        combinations.append(i**j)

c = set(combinations)

print(len(c))

# solution 9183
