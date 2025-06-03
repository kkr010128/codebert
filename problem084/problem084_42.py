import collections
n, m = map(int, input().split())
par = list(range(2 * n))

# print(par)


# union find(parには0も入れているので、par[1]=1になる)
def find(x):

    while par[x] != x:
        tmp = par[x]
        par[x] = par[par[x]]
        x = par[x]

    return x


def union(x, y):
    x1 = find(x)
    y1 = find(y)
    if x1 != y1:
        par[x1] = y1


# 各要素をunionする
for j in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

s = [0 for i in range(n + 5)]

# 1～nの親を探してsに入れていき、一番多い親を答えにする
for k in range(n):
    s[find(k)] += 1

print(max(s))
