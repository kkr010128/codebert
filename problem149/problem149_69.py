import math
n,m,x = map(int,input().split())
book = [list(map(int,input().split())) for _ in range(n)]
best = math.inf

for i in range(2**n):
    und = [0]*m
    money = 0
    for j in range(n):
        if (i>>j) & 1:
            money += book[j][0]
            for k in range(m):
                und[k] += book[j][k+1]
    if all(s>=x for s in und) and best>money:
        best = money

if best==math.inf:
    print(-1)
else:
    print(best)