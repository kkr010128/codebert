import math


def main(n: int, x: int, t: int):
    print(math.ceil(n / x) * t)


if __name__ == '__main__':
    n, x, t = map(int, input().split())
    main(n, x, t)
