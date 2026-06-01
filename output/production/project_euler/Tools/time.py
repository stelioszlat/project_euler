

def is_leap(year):
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':

    for i in range(1900, 2001):
        print(str(i) + " " + str(is_leap(i)))