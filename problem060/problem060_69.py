n,m,l = map(int,input().split())
A = [[int(i) for i in input().split()] for _ in range(n)]
B = [[int(i) for i in input().split()] for _ in range(m)]

res = [
    [sum([
        a*b for a,b in zip(A[i],list(zip(*B))[j])
    ])
    for j in range(l)]
for i in range(n)]

for r in res:
    print(*r)
