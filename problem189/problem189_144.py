import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    n, m = map(int, input().split())
    if n < 2:
        even = 0
    else:
        even = combinations_count(n, 2)
    if m < 2:
        odd = 0
    else:
        odd = combinations_count(m, 2)
    print(even + odd)


if __name__ == "__main__":
    main()
