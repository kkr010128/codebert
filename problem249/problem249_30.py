import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B, K = map(int, readline().split())

    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        B = max(0, B - K)

    print(A, B)


if __name__ == '__main__':
    main()
