# really bad method (brute force)
flag = True
number = 11
cant = False
while flag:
    cant = False
    for i in range(1, 21):
        if number % i != 0:
            cant = True
        else:
            print(i)
    if not cant:
        print(str(number) + ' SUCCESS')
        flag = False
    else:
        print(str(number) + ' can\'t be divided with 1-20')

    number += 1

# result:232792560