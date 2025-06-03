from collections import deque

n = int(input())
graph_W = []
for _ in range(n):
    graph_W.append(list(map(int, input().split())))
    
num_root = [0]*n
work_queue = deque([])
visited = set()

work_queue.append(1)
visited.add(1)
cnt = 0
while work_queue:
    here = work_queue.popleft() - 1
    num_node = graph_W[here][1]
    cnt += 1
    if num_node == 0:
        continue
    for k in range(num_node):
        num_graph = graph_W[here][k+2]
        if num_graph not in visited:
            work_queue.append(num_graph)
            visited.add(num_graph)
            num_root[num_graph-1] = num_root[here] + 1


print(1,0)
for i in range(1,n):
    if num_root[i] != 0:
        print(i+1,num_root[i])
    else:
        print(i+1,-1)
