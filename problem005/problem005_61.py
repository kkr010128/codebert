def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


while True:
    try:
        x, y = map(int, input().split())
        print(gcd(x, y), lcm(x, y))
    except:
        break

