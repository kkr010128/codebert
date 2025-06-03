#k = int(input())
import bisect
n, m, k = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
#al=[list(input()) for i in range(h)]
acum = [0]
for i in range(n):
    acum.append(al[i]+acum[i])

bcum = [0]
for i in range(m):
    bcum.append(bl[i]+bcum[i])
ans = 0
for i in range(n+1):
    rsd = k-acum[i]
    if rsd < 0:
        break
    #if rsd == 0:
    #    ans = max(ans, i)
    #    continue
    ind = bisect.bisect_right(bcum, rsd)
    ans = max(ans, i+ind-1)
print(ans)
