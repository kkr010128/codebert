import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()
    if N % 2 == 0 and S == S[: N // 2] * 2:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
