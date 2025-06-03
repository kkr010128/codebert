# Skill Up
n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

costs = []

for i in range(1 << n): #全パターン
    cost = 0
    total = [0] * m #値段とm冊の本についてのリスト
    for j in range(n):
        if (i>>j) & 1 == 1 : #iをjだけ右にシフト。j冊目を買う場合
            cost += ca[j][0]
            for k in range(m):
                total[k] += ca[j][k+1]
    if all(total[l] >= x for l in range(m)):
        costs.append(cost)

if len(costs) == 0:
    print(-1)
else:
    print(min(costs))