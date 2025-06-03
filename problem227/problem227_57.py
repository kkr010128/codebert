import sys
import heapq

n, k = map(int, input().split())
h = []
heapq.heapify(h)
for x in map(int, input().split()):
  heapq.heappush(h, x)

if n <= k:
  print(0)
  sys.exit()

ans = 0
for x in range(n - k):
  ans += heapq.heappop(h)

print(ans)
