import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    a.sort()
    a_desc = a[::-1]

    ok = 0
    ng = 2 * max(a) + 1

    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        count = 0
        i = 0
        for elem in a:
            while i < n:
                if elem + a_desc[i] >= mid:
                    i += 1
                else:
                    break
            count += i
        if count >= m:
            ok = mid
        else:
            ng = mid

    from itertools import accumulate

    a_cum = list(accumulate(a_desc))
    a_cum = a_cum[::-1] + [0]
    ans = 0
    j = n
    cnt_over = 0

    for elem in a:
        while j > 0:
            if elem + a[j - 1] > ok:
                j -= 1
            else:
                break
        cnt_over += (n - j)
        ans += a_cum[j]
        ans += elem * (n - j)

    ans += ok * (m-cnt_over)

    print(ans)


if __name__ == '__main__':
    main()
