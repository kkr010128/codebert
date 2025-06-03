import math
ans = 0

N,D = map(int,input().split())

for i in range(N):
    x,y = map(int,input().split())
    if math.sqrt(abs(x)**2 + abs(y)**2) <= D:
        ans += 1

print(ans)