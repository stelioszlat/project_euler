
def is_palindrome(number):
    pass

def triangular_of(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s

def is_perfect(n, check=False):
    divs = []
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            divs.append(i)

    for d in divs:
        sum += d

    if check:
        return sum
    else:
        if sum == n:
            return True
        return False

def is_deficient(n):
    s = is_perfect(n, True)

    if s < n:
        return True
    return False

def is_abundant(n):
    s = is_perfect(n, True)

    if s > n:
        return True
    return False

if __name__ == '__main__':
    print(is_perfect(28))
