n,m,x = map(int,input().split())
ac = [list(map(int,input().split())) for _ in range(n)]
ttlmmin = 10**8
for i in range(1<<n):
    ttlm = 0
    skl = [0]*m
    for k in range(n):
        if i & (1<<k):
            for l in range(m):
                skl[l] += ac[k][l+1]
            ttlm += ac[k][0]
    flag = True
    for l in range(m):
        if skl[l] < x:
            flag = False
            break
    if flag: ttlmmin = min(ttlmmin,ttlm)    
if ttlmmin == 10**8:
    print(-1)
else:
    print(ttlmmin)