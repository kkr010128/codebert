from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    input_list = list(map(int, input().split()))
    index = input_list[0]
    num = input_list[1]

    if num >= 1:
        nodes = input_list[2:]
        for node in nodes:
            graph[index].append(node)
            # graph[node].append(index)

visited = [-1] * (n + 1)
num = [-1] * (n + 1)
q = deque()
visited[1] = 1
num[1] = 0
q.append(1)

while q:
    index = q.popleft()
    
    for node in graph[index]:
        if visited[node] == -1:
            visited[node] = 1
            num[node] = num[index] + 1
            q.append(node)


for i, j in enumerate(num):
    if i == 0:
        continue
    print(i, j)



