# 問題：https://atcoder.jp/contests/abc143/tasks/abc143_b

n = int(input())
d = list(map(int, input().strip().split()))
res = 0
for i in range(1, n):
    for j in range(i):
        res += d[i] * d[j]
print(res)
