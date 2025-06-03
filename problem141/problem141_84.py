from math import ceil
n = int(input())
A = list(map(int,input().split()))[::-1]
mn,mx = A[0], A[0]
step = [[mn,mx]]
for i in range(1, n+1):
    mn = ceil(mn/2) + A[i]
    mx = mx + A[i]
    step.append([mn,mx])
if not mn<=1 and 1<=mx:
    print(-1)
else:
    step = step[::-1]
    A = A[::-1]
    now = 1
    ans = 1
    for i in range(1, n+1):
        now = min(step[i][1],
                  (now-A[i-1])*2)
        ans += now
    print(ans)