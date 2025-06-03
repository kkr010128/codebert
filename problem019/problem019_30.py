# coding: utf-8

import sys
from collections import deque

n, q = map(int, input().split())
total_time = 0
tasks = deque(map(lambda x: x.split(), sys.stdin.readlines()))

for task in tasks:
    task[1] = int(task[1])

try:
    while True:
        t = tasks.popleft()
        if t[1] - q <= 0:
            total_time += t[1]
            print(t[0], total_time)
        else:
            t[1] = t[1] - q
            total_time += q
            tasks.append(t)
except Exception:
    pass