import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    ans = 0
    n = len(S) // 2
    for i in range(n):
        if S[i] != S[-1 - i]:
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
