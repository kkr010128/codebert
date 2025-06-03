import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def main():
    a, b = map(int, input().split())
    print(lcm(a, b))


if __name__ == '__main__':
    main()
