import math

def main():

    a, b = [int(i) for i in input().split()]

    lo = max(1000 * a, 800 * b)
    hi = min(1000 * (a + 1), 800 * (b + 1))

    if lo < hi:
        print(math.ceil(lo / 80))
    else:
        print(-1)


main()
