# -*- coding: utf-8 -*-

import collections

n, q = map(int, raw_input().split())
prolist = [raw_input().split() for i in range(n)]
prolist = collections.deque(prolist)
time_sum = 0
while len(prolist):
    process = prolist.popleft()
    time = int(process[1])
    if time <= q:
        time_sum += time
        print "%s %d" %(process[0], time_sum)
    else:
        time_sum += q
        process[1] = str(time-q)
        prolist.append(process)