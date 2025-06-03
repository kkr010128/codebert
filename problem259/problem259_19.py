from collections import defaultdict, deque

N, u, v  = map(int, input().split())
way = defaultdict(list)
for _ in range(N-1):
    a, b =  map(int, input().split())
    
    way[a].append(b)
    way[b].append(a)
seen1 = [-1]*N
seen2 = [-1]*N
seen1[u-1] = 0
seen2[v-1]= 0

queue = deque([u])
while queue:
    q = queue.popleft()
    for i in way[q]:
        if seen1[i-1]==-1:
            queue.append(i)
            seen1[i-1] = seen1[q-1]+1

queue = deque([v])
while queue:
    q = queue.popleft()
    for i in way[q]:
        if seen2[i-1]==-1:
            queue.append(i)
            seen2[i-1] = seen2[q-1]+1
            
#print(way)
#print(seen1)
#print(seen2)
for i in range(N):
    if seen1[i]>=seen2[i]:
        seen2[i] = -1
print(max(seen2)-1)