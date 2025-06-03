N,M = map(int,input().split())
d,ans,wrong = [0]*N,0,0
for _ in range(M):
    p,s = input().split()
    p = int(p)-1
    if d[p] != -1:
        if s == "WA":
            d[p] += 1
        else:
            wrong += d[p]
            d[p] = -1
            ans += 1
print(ans,wrong)