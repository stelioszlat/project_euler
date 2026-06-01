# brute forced solution

products = []
palindromes = []

# calculate products
for i in range(100, 1000):
    for j in range(100, 1000):
        products.append(i * j)

# for p in products:
#     [int(d) for d in str(p)]

# print(products)

# check for palindromes

for p in products:
    if p == int(str(p)[::-1]):
        palindromes.append(p)

# print(palindromes)
print(max(palindromes))

#  result : 906609


