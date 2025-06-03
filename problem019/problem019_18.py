from collections import deque

n, q = map(int, input().split())
t = 0
queue = deque([])
for _ in range(n):
    name, time = input().split()
    time = int(time)
    queue.append([name, time])
while len(queue):
    if queue[0][1] > q:
        queue[0][1] -= q
        t += q
        queue.rotate(-1)
    else:
        t += queue[0][1]
        queue[0][1] = t
        print(" ".join(list(map(str, queue.popleft()))))