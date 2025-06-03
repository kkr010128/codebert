N, M = map(int, input().split())
ABs = [tuple(map(int, input().split())) for _ in range(M)]

par = [i for i in range(N)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        par[x] = y

for a, b in ABs:
    unite(a-1, b-1)

for x in range(N):
    find(x)

print(len(set(par))-1)
