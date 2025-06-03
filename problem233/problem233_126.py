import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    P = list(map(int, readline().split()))
    cur = N + 1
    ans = 0
    for x in P:
        if cur > x:
            ans += 1
            cur = x

    print(ans)

if __name__ == '__main__':
    main()
