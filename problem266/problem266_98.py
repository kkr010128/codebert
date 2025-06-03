x = int(open(0).read().split()[0])

import heapq

s = {0} 
hq = [0]

prices = list(range(100, 106))

tmp = 0

while tmp<x:
    tmp = heapq.heappop(hq)
    for price in prices:
        new = tmp+price
        if new not in s:
            s.add(new)
            heapq.heappush(hq, new)

print(int(tmp == x))