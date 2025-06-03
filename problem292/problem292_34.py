import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *D = map(int, read().split())

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += D[i] * D[j]

    print(ans)
    return


if __name__ == '__main__':
    main()
