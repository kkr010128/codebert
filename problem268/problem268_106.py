import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    MOD = 1000000007
    N, *A = map(int, read().split())
    C = [0] * (N + 1)
    C[0] = 3
    ans = 1
    for a in A:
        ans = ans * C[a] % MOD
        if ans == 0:
            print(0)
            return
        C[a] -= 1
        C[a + 1] += 1

    print(ans)

    return


if __name__ == '__main__':
    main()
