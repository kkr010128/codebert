# coding: utf-8

import sys
from collections import deque

n, q = map(int, input().split())
total_time = 0
tasks = deque(map(lambda x: x.split(), sys.stdin.readlines()))

try:
    while True:
        t = tasks.popleft()
        if int(t[1]) - q <= 0:
            total_time += int(t[1])
            print(t[0], total_time)
        else:
            t[1] = str(int(t[1]) - q)
            total_time += q
            tasks.append(t)
except Exception:
    pass