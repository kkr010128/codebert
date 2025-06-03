n,m = map(int,input().split())
hi = [0] + list(map(int,input().split()))
judge = [0]+[1]*(n)

for _ in range(m):
    a,b = map(int, input().split())
    if hi[a] >= hi[b]:
        judge[b] = 0
    if hi[a] <= hi[b]:
        judge[a] = 0
print(sum(judge))
