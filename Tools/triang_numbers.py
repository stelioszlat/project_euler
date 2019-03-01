
# get the nth triangular number
def get_triang_number(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s


if __name__ == '__main__':
    print(get_triang_number(7))
