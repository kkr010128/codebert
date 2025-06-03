N, M = map(int, input().split())
t = [-1] * N
import sys
sys.setrecursionlimit(10 ** 9)

root = [-1] * N

def parent(x):
    if root[x] < 0:
        return x
    root[x] = parent(root[x])
    return root[x]


def union(x, y):
    x_parent = parent(x)
    y_parent = parent(y)
    if x_parent == y_parent:
        return
    root[x_parent] += root[y_parent]
    root[y_parent] = x



for i in range(M):
    a,b = map(int, input().split())
    union(a-1,b-1)
ans = -1
for i in root:
    if i < 0:
        ans += 1
print(ans)