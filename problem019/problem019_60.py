#coding:utf-8
#1_3_B
from collections import deque

n, quantum = map(int, input().split())
q = deque()
total_time = 0
for i in range(n):
    name, time = input().split()
    q.append([name, int(time)])

while q:
    ps_name, ps_time = q.popleft()
    if ps_time <= quantum:
        total_time += ps_time
        print(ps_name, total_time)
    else:
        total_time += quantum
        ps_time -= quantum
        q.append([ps_name, ps_time])