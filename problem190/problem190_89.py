import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    N = len(S)

    if (
        S == S[::-1]
        and S[: (N - 1) // 2] == S[: (N - 1) // 2][::-1]
        and S[(N + 1) // 2 :] == S[(N + 1) // 2 :][::-1]
    ):
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
