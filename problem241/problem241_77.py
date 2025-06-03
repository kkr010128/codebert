import sys
import itertools
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)
 
H,W = map(int,readline().split())
grid = ''
grid += '#'* (W+2)
for _ in range(H):
    grid += '#' + readline().decode().rstrip() + '#'
grid += '#'*(W+2)
L = len(grid)
INF = float('inf')

def bfs(start):
    dist = [-INF] * L
    q = [start]
    dist[start] = 0
    while q:
        qq = []
        for x,dx in itertools.product(q,[1,-1,W+2,-W-2]):
            y = x+dx
            if dist[y] != -INF or grid[y] == '#':
                continue
            dist[y] = dist[x] + 1
            qq.append(y)
        q = qq
    return max(dist) 

ans = 0
for i in range(L):
    if grid[i] == '.':
        start = i
        max_dist = bfs(start)
        ans = max(ans,max_dist)
print(ans)