from Tools.factors import factorial

number = factorial(100)

num_list = [int(d) for d in str(number)]

sum = 0
for n in num_list:
    sum += n

print(sum)

# answer: 648 
