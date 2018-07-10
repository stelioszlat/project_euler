# brute forced solution

products = []

# calculate products
for i in range(100, 1000):
    for j in range(100, 1000):
        products.append(i * j)

for p in products:
    [int(d) for d in str(p)]

print(products)

# check for palindromes