A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

oldp = min(a)+min(b)

for _ in range(M):
    x, y, cp = map(int,input().split())
    p = a[x-1]+b[y-1]-cp
    if oldp > p:
        oldp = p

print(oldp)