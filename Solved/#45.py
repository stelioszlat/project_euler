
triang = []
pentag = []
hexag = []
min = 286
max = 10000
while True:
    for i in range(min, max):
        triang.append(i*(i+1)/2)
        print(triang[-1])
        pentag.append(i*(3*i-1)/2)
        print(pentag[-1])
        hexag.append(i*(2*i-1))
        print(hexag[-1])
        print()


    for i in triang:
        if i in pentag:
            if i in hexag:
                print(i)
                exit(0)

    min = max
    max += 10000

# solution: 1533776805