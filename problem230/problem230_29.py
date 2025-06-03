from bisect import *

N, D, A = map(int, input().split())

data = []
for _ in range(N):
    x, h = map(int, input().split())
    data.append((x,h))
data.sort()

X = []
H = []
for x, h in data:
    X.append(x)
    H.append(h)

Imos = [0]*(N+1)
cnt = 0
damage = 0
res = 0
for i in range(N):
    damage -= Imos[i]*A
    h = H[i] - damage
    x = X[i]
    if h > 0:
        cnt = h//A + (h%A!=0)
        p = min(bisect_right(X, x+2*D)-1, N-1)
        Imos[p+1] += cnt
        damage = damage + cnt * A
        res += cnt
print(res)
