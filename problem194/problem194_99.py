h,w=map(int,input().split())
grid=[[1 if s=='#' else 0 for s in list(input())] for i in range(h)]
#print(grid)
maxi=10**5
from collections import deque
visited=[[maxi]*w for _ in range(h)]
def bfs(s):
    q=deque()
    q.append(s)
    visited[s[0]][s[1]]=grid[s[0]][s[1]]
    for r in range(h):
        for c in range(w):
            if r>=1:
                visited[r][c]=min(visited[r][c],visited[r-1][c]+grid[r][c])
                if grid[r-1][c]==1:
                    visited[r][c]=min(visited[r][c],visited[r-1][c])
            if c>=1:
                visited[r][c]=min(visited[r][c],visited[r][c-1]+grid[r][c])
                if grid[r][c-1]==1:
                    visited[r][c]=min(visited[r][c],visited[r][c-1])
            

bfs([0,0])
print(visited[-1][-1])