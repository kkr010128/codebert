n = int(input())
G = {i:[] for i in range(1, n+1)}
for _ in range(n):
    ukv = list(map(int, input().split()))
    u = ukv[0]
    k = ukv[1]
    for i in range(2, 2+k):
        G[u].append(ukv[i])
        
d = [-1 for _ in range(n+1)]
f = [-1 for _ in range(n+1)]
counter = 0

def dfs(n):
    global counter
    counter += 1
    d[n] = counter
    
    for n_i in G[n]:
        if d[n_i]==-1:
            dfs(n_i)
            
    counter += 1
    f[n] = counter

for i in range(1, n+1):
    if d[i]==-1:
        dfs(i)

for id_i, (d_i, f_i) in enumerate(zip(d[1:], f[1:]), 1):
    print(id_i, d_i, f_i)
