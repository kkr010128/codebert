#
# 10d
#
import math


def main():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    d1 = 0
    d2 = 0
    d3 = 0
    dn = 0
    for i in range(n):
        d1 += abs(x[i] - y[i])
        d2 += (x[i] - y[i])**2
        d3 += abs(x[i] - y[i])**3
        dn = max(dn, abs(x[i] - y[i]))

    d2 = math.sqrt(d2)
    d3 = math.pow(d3, 1/3)
    print(f"{d1:.5f}")
    print(f"{d2:.5f}")
    print(f"{d3:.5f}")
    print(f"{dn:.5f}")


if __name__ == '__main__':
    main()
