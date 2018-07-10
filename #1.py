i = 0
j = 0
factor = 1
s = 0
list3 = []
list5 = []

while i < 1000:
    i = 3 * factor
    if i < 1000:
        list3.append(i)
    factor += 1

factor = 0

while j < 1000:
    j = 5 * factor
    if j < 1000:
        list5.append(j)
    factor += 1

list3.extend(list5)
list3 = set(list3)
# print(list3)

for i in list3:
    s += i

print(s)
