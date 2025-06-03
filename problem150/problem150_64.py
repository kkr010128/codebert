n,k = map(int,input().split())
a = list(map(int,input().split()))

next = [[0]*n for _ in range(60)]

for v in range(n):
    next[0][v] = a[v]-1
for d in range(60-1):
    for v in range(n):
        next[d+1][v] = next[d][next[d][v]]
        
v = 0
for d in range(60):
    if k>>d&1:
        v = next[d][v]
        
print(v+1)