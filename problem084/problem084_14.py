n,m = list(map(int, input().split()))
parents = [-1] * (n + 1)
def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parents[x] > parents[y]:
        x, y = y, x

    parents[x] += parents[y]
    parents[y] = x

def same(x, y):
    return find(x) == find(y)

for _ in range(m):
    a,b = list(map(int, input().split()))    
    union(a,b)

print(-min(parents[1:]))