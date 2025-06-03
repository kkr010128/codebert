# 問題：https://atcoder.jp/contests/abc142/tasks/abc142_b

n, k = map(int, input().strip().split())
h = list(map(int, input().strip().split()))
res = 0
for i in range(n):
    if h[i] < k:
        continue
    res += 1
print(res)

