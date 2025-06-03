import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = map(int, readline().split())

    ans = (N + M) * (N + M - 1) // 2 - N * M

    print(ans)
    return


if __name__ == '__main__':
    main()
