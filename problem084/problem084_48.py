n, m = map(int, input().split())
 
root = [-1]*n
def r(x):
    if root[x] < 0:
        return x
    else:
        root[x] = r(root[x])
        return root[x]
 
def unite(x, y):
    x = r(x)
    y = r(y)
    if x == y:
        return
    root[x] += root[y]
    root[y] = x
 
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    unite(a, b)
 
ans = 0
for i in range(n):
    ans = max(ans, -root[i])
 
print(ans)
