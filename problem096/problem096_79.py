#B問題

import math

distance = 0
ans = 0
n, d = map(int, input().split())
x = [input().split() for l in range(n)]

#リストの中にリストがある時→A[i][j]のように表現
for i in range(n):
    distance = math.sqrt(pow(int(x[i][0]),2)+pow(int(x[i][1]),2))
    if distance <= d:
        ans += 1
print(ans)