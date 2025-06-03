from collections import deque
import math
import copy
#https://qiita.com/ophhdn/items/fb10c932d44b18d12656

def max_dist(input_maze,startx,starty,mazex,mazey):
    input_maze[starty][startx]=0
    que=deque([[starty,startx]])
#    print(que)
    while que:
#        print(que,input_maze)
        y,x=que.popleft()
        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            nexty,nextx=y+i,x+j
            if (nexty>=0) & (nextx>=0) & (nextx<mazex) & (nexty<mazey):
                dist=input_maze[nexty][nextx]
                if dist!=-1:
                    if (dist>input_maze[y][x]+1) & (dist > 0):
                        input_maze[nexty][nextx]=input_maze[y][x]+1
                        que.append([nexty,nextx])
#    print(que)
#    print(max(list(map(lambda x: max(x),copy_maze))))
    return max(list(map(lambda x: max(x),copy_maze)))

h,w =list(map(int,input().split()))
maze=[list(input()) for l in range(h)]

# Maze preprocess
for y in range(h):
    for x in range(w):
        if maze[y][x]=='.':
            maze[y][x]=math.inf
        elif maze[y][x] == '#':
            maze[y][x]=int(-1)

results = []

for y in range(h):
    for x in range(w):
        if maze[y][x]==math.inf:
            copy_maze = copy.deepcopy(maze)
            max_dist_result = max_dist(copy_maze,x,y,w,h)
            results.append(int(max_dist_result))
            #print(max_dist_result)

print(max(results))

