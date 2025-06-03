# vim: fileencoding=utf-8

import math


def main():
    a = int(input())
    res = a + math.pow(a, 2) + math.pow(a, 3)
    print(int(res))


if __name__ == "__main__":
    main()
