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

    ans = [0] * len(S)
    for i, c in enumerate(S):
        ans[i] = chr((ord(c) - 65 + N) % 26 + 65)

    print(''.join(ans))
    return


if __name__ == '__main__':
    main()
