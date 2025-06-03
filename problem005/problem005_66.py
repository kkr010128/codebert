import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    for i in sys.stdin.readlines():
        a, b = [int(x) for x in i.split()]
        print(gcd(a, b), lcm(a, b))


if __name__ == '__main__':
    main()