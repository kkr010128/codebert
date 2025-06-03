import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = list(map(int, readline().split()))

    cnt = [0] * 3
    ans = 1

    for x in a:
        p = cnt.count(x)
        if p == 0:
            return print(0)
        ans *= p
        ans %= MOD
        cnt[cnt.index(x)] += 1

    print(ans)


if __name__ == '__main__':
    main()
