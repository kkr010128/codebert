D = int(input())
c = list(map(int, input().split()))

s = []
for _ in range(D):
    s.append(list(map(int, input().split())))

t = []
for _ in range(D):
    t.append(int(input()))

# last(d, i)を計算するためのメモ
dp = [0] * 26


def dec(d):
    # d日の終わりに起こる満足度の減少計算の関数
    s = 0
    for j in range(26):
        s += c[j] * (d - dp[j])

    return s


# vは満足度
v = 0
for i in range(D):
    # 初日の満足度
    if (i == 0):
        v += s[i][t[i] - 1]
        # 開催されたコンテストの日付をメモ
        dp[t[i] - 1] = (i + 1)
        v -= dec(i + 1)
        print(v)
        continue

    # elif (0 < i and i < D - 1):
    v += s[i][t[i] - 1]
    dp[t[i] - 1] = (i + 1)
    v -= dec(i + 1)
    print(v)
