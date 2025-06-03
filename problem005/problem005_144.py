def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)


def lcm(x,y):
    return x/gcd(x, y)*y


while True:
    try:
        x, y = map(int, raw_input().split())
    except EOFError:
        break

    print "%d %d" % (gcd(x, y), lcm(x, y))