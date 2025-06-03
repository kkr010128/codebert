import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def main():
    K = int(input())
    s = sum([gcd(i+1, j+1, k+1) for i in range(K) for j in range(K) for k in range(K)])

    print(s)


if __name__=="__main__":
    main()
