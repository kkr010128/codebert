def solve_145e():
    from collections import namedtuple
    from operator import attrgetter
    import sys
    input = sys.stdin.readline

    Food = namedtuple('Food', 'time_to_eat deliciousness')

    N, T = map(int, input().split())
    foods = []
    for _ in range(N):
        row = map(int, input().split())
        foods.append(Food(*row))
    foods.sort(key=attrgetter('time_to_eat'))
    # 同じ料理の組を食べるなら時間のかかるものを後回しにしても結果は悪くならない

    dp = [-1] * T
    dp[0] = 0
    # dp[time]:=timeに食べ終わる注文の仕方で得られる最大満足度

    ma = 0  # 回答候補
    ca = 0  # フィニッシュ前候補
    for food in foods:
        # これでフィニッシュの場合
        ma = max(ma, ca + food.deliciousness)

        # まだ食べる場合
        for time in range(T - 1 - food.time_to_eat, -1, -1):
            if ~dp[time]:
                when_eat = dp[time] + food.deliciousness
                if dp[time + food.time_to_eat] < when_eat:
                    dp[time + food.time_to_eat] = when_eat
                    ca = max(ca, when_eat)

    print(ma)
    return


if __name__ == '__main__':
    solve_145e()
