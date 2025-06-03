import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    ans = 0
    p = 1
    for _ in range(60):
        n = 0
        for i in range(N):
            A[i], d = A[i] // 2, A[i] % 2
            n += d
        ans = (ans + n * (N - n) * p) % MOD
        p = p * 2 % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
