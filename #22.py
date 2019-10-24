
letter_score = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

with open("p022_names.txt") as f:

    names = f.readline()

print(names)
names_list = names.split(',')
names_list.sort()

names_score = []
position = 0

for name in names_list:
    position += 1
    s = 0
    for letter in name:
        if letter != '\"':
            s += letter_score.get(letter)
            print(letter)
    names_score.append(s * position)


print(names_list)
print(names_score)
print(sum(names_score))

# solution: 871198282
