from collections import deque

n,limit = map(int,input().split())
total_time = 0
queue = deque()
for _ in range(n):
    p,t = input().split()
    queue.append([p,int(t)])

while len(queue) > 0:
    head = queue.popleft()
    if head[1] <= limit:
        total_time += head[1]
        print('{} {}'.format(head[0],total_time))
    else:
        head[1] -= limit
        total_time += limit
        queue.append(head)
