import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    B = [0] * (N + 1)
    for a in A:
        B[a] += 1

    total = 0
    for b in B:
        total += b * (b - 1) // 2

    ans = [0] * N
    for i, a in enumerate(A):
        ans[i] = total - (B[a] - 1)

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()
