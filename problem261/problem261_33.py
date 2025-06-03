import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    n = len(S)

    ans = 0
    for i in range(n // 2):
        if S[i] != S[n - 1 - i]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
