import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, X, Y = mapint()
X, Y = X-1, Y-1
dist = [0]*(N-1)
for i in range(N-1):
    for j in range(i+1, N):
        d = min(j-i, abs(i-X)+abs(j-Y)+1, abs(i-Y)+abs(j-X)+1)
        dist[d-1] += 1
for k in range(N-1):
    print(dist[k])