N, M = map(int, input().split())
Pajew = [i for i in range(N)]
import sys
sys.setrecursionlimit(1000000)

def find(x, Pajew):
    if Pajew[x] == x:
        return x
    else:
        a = find(Pajew[x], Pajew)
        Pajew[x] =a
        return a

def unite(x, y):
    x = find(x, Pajew)
    y = find(y, Pajew)
    if x != y:
        Pajew[x] = y

for _ in range(M):
    a, b = map(int, input().split())
    unite(a-1, b-1)

grou = 0
for i in range(N):
    if i == Pajew[i]:
        grou +=1


print(grou-1)