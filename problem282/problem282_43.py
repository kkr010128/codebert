def main():
    from collections import namedtuple
    from operator import attrgetter

    Dish = namedtuple('Dish', 'time deliciousness')

    N, T = map(int, input().split())
    dishes = []
    for _ in range(N):
        a, b = map(int, input().split())
        d = Dish(time=a, deliciousness=b)
        dishes.append(d)

    dishes.sort(key=attrgetter('time'))

    dp = [0] * T
    ma = 0
    ret = 0
    for d in dishes:
        ret = max(ret, ma + d.deliciousness)
        for t in range(T - 1, d.time - 1, -1):
            dp[t] = max(dp[t], dp[t - d.time] + d.deliciousness)
            ma = max(ma, dp[t])
    print(ret)


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
