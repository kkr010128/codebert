import math
a,b = map(int, input().split())
ans = 10000
for i in range(1010):
    if math.floor(i*0.08) == a and math.floor(i*0.1) == b:
        ans = i
        break

if ans == 10000:
    print(-1)
else:
    print(ans)