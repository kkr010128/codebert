import sys
input = sys.stdin.readline
N = int(input())
robo_range = []
for _ in range(N):
  X, L = map(int,input().rstrip().split())
  robo_range.append((X-L,X+L))
robo_range_sort = sorted(robo_range,key = lambda x:x[1])
ans = 0
cut = -float('inf')
for i in range(N):
  if cut <= robo_range_sort[i][0]:
    ans += 1
    cut = robo_range_sort[i][1]
print(ans)