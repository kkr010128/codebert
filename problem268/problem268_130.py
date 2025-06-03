import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    MOD = 1000000007
    N, *A = map(int, read().split())

    ans = 1
    C = [0] * (N + 1)
    C[0] = 3
    for a in A:
        ans = ans * C[a] % MOD
        C[a] -= 1
        C[a + 1] += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
