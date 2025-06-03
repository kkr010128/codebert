import sys
import math
import time
readline = sys.stdin.readline


def main():
    listSum = [1, 3, 6]
    k = int(input())
    sumGCD = 0
    for a in range(1, k + 1):
        for b in range(a, k + 1):
            for c in range(b, k + 1):
                sumGCD += gcd(a, b, c) * listSum[len(set([a, b, c])) - 1]
    print(sumGCD)


def gcd(a, b, c):
    return math.gcd(math.gcd(a, b), c)


if __name__ == '__main__':
    s = time.time()
    main()
    # print(time.time() - s)
