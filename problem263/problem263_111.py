import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())
    M = 61
    C = [0] * M
    for a in A:
        a = str(format(a, 'b'))
        for i, d in enumerate(reversed(a)):
            if d == '1':
                C[i] += 1

    ans = 0
    p = 1
    for c in C:
        ans = (ans + c * (N - c) * p) % MOD
        p = p * 2 % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
