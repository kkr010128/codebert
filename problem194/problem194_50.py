h, w = map(int,input().split())

maze = []
for i in range(h):
    t = list(input())
    maze.append(t)
    
dx = [1, 0]
dy = [0, 1]


dp = [[10000]*w for i in range(h)]
if maze[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0

for x in range(w):
    for y in range(h):
        for dxi, dyi in zip(dx, dy):
            if not (0<=x+dxi<w and 0<=y+dyi<h):
                continue
            dp[y+dyi][x+dxi] = min(dp[y+dyi][x+dxi], dp[y][x]+(maze[y][x]=="." and maze[y+dyi][x+dxi]=="#"))
            
#print(*dp)
print(dp[h-1][w-1])