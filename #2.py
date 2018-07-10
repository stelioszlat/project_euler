x = 4000000
i = 0
fib = [0, 1, 1]
s = 0

while i < x:
    fib.append(fib[-1] + fib[-2])
    i = fib[-1]

# print(fib)

for i in fib:
    if i % 2 == 0:
        s += i

print(s)
