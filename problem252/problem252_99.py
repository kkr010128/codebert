import bisect

if __name__ == '__main__':
    def check(mid):
        count = 0
        for i in range(n):
            position = bisect.bisect_left(a, (mid - a[i]))
            count += (n - position)
        return count < m


    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    # 左手でa[i]の手を握るとする
    # a[i]を持っているときに和がx未満になるときの右手の数字はx - a[i]未満の数字である
    # lower_bound
    # この値をNから引くことで和がx以上になるペアの個数がわかる
    # この値の合計がM未満になればそこが最大の幸福度である

    # 要するに、M個のペアを作るためには最大いくらの和を採用できるかを二分探索する

    ng = 0
    ok = 10 ** 5 * (n + 1)

    while 1 < abs(ok - ng):
        # mid -> boundとなる和。これより大きい和をもつペアをM個作れるかを判定する
        mid = (ok + ng) // 2
        c = check(mid)
        # ペアの個数がmより小さい場合は、okの範囲を下げる
        if c:
            ok = mid
        # そうでない場合はまだ余裕があるので、ngをあげる
        else:
            ng = mid

    # ここが終了した時点でngにはm個以上のペアを作るための最大のboundが入っている

    # upper_boundで左手にa[i]がある場合のng - a[i]の数を判定する
    # ansに求めた数 * a[i] + 右手に持つ幸福度の総和を足す
    # mから求めた数を引く

    ans = 0
    sum_array = [0] * (n + 1)
    # 累積和で高速化をする
    # (x + a[i]) + (x + a[i + 1) + (x + a[i + 2]).....
    #   -> (x * 個数) * (a[i] + a[i + 1] + a[i + 2])

    for i in range(n):
        sum_array[i + 1] = sum_array[i] + a[i]
    for i in range(n):
        position = bisect.bisect_right(a, ng - a[i])
        ans += (n - position) * a[i] + sum_array[n] - sum_array[position]
        m -= (n - position)

    ans += ng * m
    print(ans)
