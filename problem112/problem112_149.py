MOD = 10 ** 9 + 7


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: abs(x), reverse=True)

    res = 1

    if k == n:
        for e in a:
            res *= e
            res %= MOD
    elif max(a) < 0:
        if k % 2 == 1:
            for i in range(n - k, n):
                res *= a[i]
                res %= MOD
        else:
            for i in range(k):
                res *= a[i]
                res %= MOD
    else:
        plus_a = [e for e in a if e >= 0]
        minus_a = [e for e in a if e < 0]

        minus_cnt = min(k, len(minus_a))
        minus_cnt -= minus_cnt % 2
        plus_cnt = k - minus_cnt

        minus_a = minus_a[:minus_cnt]
        minus_a.reverse()

        max_change_cnt = min(minus_cnt, len(plus_a) - plus_cnt)
        max_change_cnt -= max_change_cnt % 2
        change_cnt = 0
        while change_cnt < max_change_cnt:
            if plus_a[plus_cnt + change_cnt] * plus_a[plus_cnt + change_cnt + 1]\
                    <= minus_a[change_cnt] * minus_a[change_cnt + 1]:
                break
            change_cnt += 2

        for i in range(change_cnt, minus_cnt):
            res *= minus_a[i]
            res %= MOD

        for i in range(plus_cnt + change_cnt):
            res *= plus_a[i]
            res %= MOD

    print(res)


main()
