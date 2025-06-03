
from collections import deque

n, q = map(int, input().split())
procs = deque([])

for i in range(n):
    name, time = input().split()
    time = int(time)
    procs.append([name, time])

total = 0

while procs:
    procs[0][1] -= q

    if procs[0][1] > 0:
        total += q
        procs.append(procs.popleft())
    else:
        total += q + procs[0][1]
        print(procs[0][0], total)
        procs.popleft()