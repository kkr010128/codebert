import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())

root = [-1] * N


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


def size(x):
    return -r(x)


for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    unite(a, b)

max_size = -min(root)
print(max_size)
