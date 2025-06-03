import math
import itertools
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)
n = int(input())
adj = {}
for i in range(1, n+1):
    x, y = map(int, input().split())
    adj[i] = (x, y)
dd = {}
ans = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        dist = distance(adj[i], adj[j])
        ans += dist
print(format((2 * ans) / n, '.10f'))