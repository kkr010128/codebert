n, k = map(int, input().split())
p = list(map(int, input().split()))
p = [_p-1 for _p in p]
c = list(map(int, input().split()))

ans = -float('inf')

visited = [False] * n
ss = []
for i in range(n):
    if visited[i]: continue
    cur = i
    s = []
    while not visited[cur]:
        visited[cur] = True
        s.append(c[cur])
        cur = p[cur]
    ss.append(s)

for s in ss:
    m = len(s)
    cumsum = [0] * (m*2+1)
    for i in range(2*m):
        cumsum[i+1] = cumsum[i] + s[i%m]
    
    amari = [-float('inf')] * m
    for i in range(m):
        for j in range(m):
            amari[j] = max(amari[j], cumsum[i+j] - cumsum[i])
    
    for r in range(0, m):
        if r > k: continue
        q = (k-r)//m
        if r==0 and q==0:
            continue
        
        if cumsum[m] > 0:
            ans = max(ans, amari[r] + cumsum[m]*q)
        elif r > 0:
            ans = max(ans, amari[r])

print(ans)
