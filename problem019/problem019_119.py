# coding=utf-8
from collections import deque

n, q = map(int, input().split())
queue = deque()
total_time = 0

for i in range(n):
    name, time = input().split()
    queue.append([name, int(time)])

while queue:
    poped = queue.popleft()
    if poped[1] > q:
        queue.append([poped[0], poped[1] - q])
        total_time += q
    else:
        total_time += poped[1]
        print(poped[0], total_time)