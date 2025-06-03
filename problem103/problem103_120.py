n = int(input())
a = list(map(int, input().split()))
a.append(0)
m = 1000
s = 0

for i in range(n):
    if a[i] < a[i + 1]: #翌日上がるなら最大限買う
        sv = m//a[i]
        m -= a[i]*sv
        s += sv
    else:               #翌日同じか下がるなら全て売る
        m += a[i]*s
        s = 0

print(m)