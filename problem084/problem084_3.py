from sys import stdin


input = stdin.readline


N, M = map(int, input().split())
friends = [tuple(map(int, inp.strip().split())) for inp in stdin.read().splitlines()]
father = [-1] * N


def getfather(x):
    if father[x] < 0: return x
    father[x] = getfather(father[x])
    return father[x]


def union(x, y):
    x = getfather(x)
    y = getfather(y)
    if x != y:
        if father[x] > father[y]:
            x,y = y,x
        father[x] += father[y]
        father[y] = x;


for a, b in friends:
    union(a - 1, b - 1)
# print(max(Counter([getfather(i) for i in range(N)]).values()))
print(max([-father[getfather(i)] for i in range(N)] or [0]) )