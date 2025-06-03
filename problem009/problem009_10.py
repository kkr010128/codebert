import collections
n = int(input())
adj_list = []

for _ in range(n):
    adj = list(map(int, input().split(" ")))
    adj_list.append([c - 1 for c in adj[2:]])

distances = [-1 for _ in range(n)]
queue = collections.deque()
queue.append(0)
distances[0] = 0

while queue:
    p = queue.popleft()

    for next_p in adj_list[p]:
        if distances[next_p] == -1:
            distances[next_p] = distances[p] + 1
            queue.append(next_p)

for i in range(n):
    print(i+1, distances[i])
