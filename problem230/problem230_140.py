import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, d, a = list(map(int, readline().split()))
    xh = [list(map(int, readline().split())) for _ in range(n)]

    from operator import itemgetter, add
    import bisect

    xh.sort(key=itemgetter(0))
    coordinate = [xh[i][0] for i in range(n)]
    hp = [xh[i][1] for i in range(n)]

    ans = 0
    dmg_cur = 0
    dmg_cum = [0] * (n + 1)

    for i in range(n):
        x = coordinate[i]
        h = hp[i]

        dmg_cur += dmg_cum[i]
        h -= dmg_cur

        if h > 0:
            num = (h + a - 1) // a
            ans += num
            dmg = a * num
            dmg_cur += dmg
            range_left = x
            range_right = x + 2 * d
            index_right = bisect.bisect_right(coordinate, range_right)
            dmg_cum[index_right] -= dmg
    print(ans)


if __name__ == '__main__':
    main()
