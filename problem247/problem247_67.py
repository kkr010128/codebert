import sys

read = sys.stdin.read


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N, M, *A = map(int, read().split())
    G = A.copy()

    while not any(x % 2 for x in G):
        G = [i // 2 for i in G]

    if not all(x % 2 for x in G):
        print(0)
        exit(0)

    total = 1

    for x in A:
        total = lcm(total, x // 2)

    print((M // total + 1) // 2)


if __name__ == '__main__':
    main()
