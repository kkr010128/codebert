import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    n = int(readline())
    count = Counter()

    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                a = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
                count[a] += 1

    for i in range(1, n + 1):
        print(count[i])


if __name__ == '__main__':
    main()
