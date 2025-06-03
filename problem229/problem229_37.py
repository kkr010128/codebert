

def read_input():
    h, n = map(int, input().split())
    magic = {}
    for i in range(n):
        a, b = map(int, input().split())
        magic[i] = (a, b)

    return h, n, magic


def submit():
    h, n, magic = read_input()

    dp = [float('inf') for _ in range(h + 1)]
    dp[h] = 0

    for i in reversed(range(1, h + 1)):
        for a, b in magic.values():
            # 更新する
            # max(0, i - a)のHPにより少ない魔力消費量で行き着ければ更新する
            rest = max(0, i - a)
            if dp[rest] > dp[i] + b:
                dp[rest] = dp[i] + b

    print(dp[0])


submit()