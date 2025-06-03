import math
import bisect
 
n,d,a = map(int,input().split())
x = [0]*n
h = [0]*n
for i in range(n):
    x[i] , h[i] = map(int, input().split())
    
itv = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    itv[i][0] = x[i]
    itv[i][1] = h[i]
itv.sort()
ans = 0

x.sort()
x.append(1145141919810)
h.append(0)

imos = [0]*(n+1)

atk = math.ceil(itv[0][1]/a)
imos[0] += atk * a
b = bisect.bisect(x,itv[0][0] + (2*d))
imos[b] -= atk * a
ans += atk
    
for i in range(1,n):
    atk = 0
    imos[i] += imos[i-1]
    if itv[i][1] > imos[i]:
        atk = math.ceil((itv[i][1]-imos[i])/a)
        imos[i] += atk * a
        b = bisect.bisect(x,itv[i][0] + (2*d))
        imos[b] -= atk * a
    ans += atk

print(ans)