import itertools

n,m,x = (int(i) for i in input().split())
A = []
for i in range(n):
    A.append([int(i) for i in input().split()])

ans = float('inf')

for p in itertools.product(range(2), repeat=n):
    knowledges = [0 for _ in range(m)]
    tmp = 0

    for i,a in zip(p,A):
        if i == 0: continue
        tmp += a[0]
        for j,anm in enumerate(a[1:]): knowledges[j] += anm
    
    if all([a >= x for a in knowledges]):
        ans = min(ans, tmp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
