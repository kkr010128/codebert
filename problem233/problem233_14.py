N,*P = map(int, open(0).read().split())
m = P[0]
ans = 0
for x in P:
    if x <= m:
        m = x
        ans += 1
print(ans)