import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    S = set(A)

    if len(S) == N:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
