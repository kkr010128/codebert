n, k = map(int, input().split())
P = list(map(int, input().split()))
ans = 0
E = []

for p in P:
    E.append(p*(p+1)/(2*p))

cumsumE = [0]
for e in E:
    cumsumE.append(cumsumE[-1] + e)

for i in range(0, n+1-k):
    ans = max(ans, cumsumE[i+k]-cumsumE[i])
print(ans)