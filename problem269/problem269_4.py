import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    t1, t2 = map(int, readline().split())
    a1, a2 = map(int, readline().split())
    b1, b2 = map(int, readline().split())

    if a1 < b1:
        a1, b1 = b1, a1
        a2, b2 = b2, a2

    if a2 > b2:
        return print(0)
    else:
        d1 = t1 * a1 + t2 * a2
        d2 = t1 * b1 + t2 * b2
        if d1 == d2:
            return print("infinity")
        elif d2 > d1:
            ans = 1
            diff = d2 - d1
            x = t1 * (a1 - b1)
            cnt = x // diff
            ans += cnt * 2
            if x % diff == 0:
                ans -= 1
            return print(ans)
        else:
            return print(0)


if __name__ == '__main__':
    main()
