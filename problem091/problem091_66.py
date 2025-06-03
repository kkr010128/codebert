from itertools import combinations

n = int(input())
L = list(map(int, input().split()))

cnt = 0
for edges in list(combinations(L, 3)):
  if len(set(edges)) != 3:
    continue
  
  e1 = edges[0] < edges[1] + edges[2]
  e2 = edges[1] < edges[0] + edges[2]
  e3 = edges[2] < edges[0] + edges[1]
  
  if e1 and e2  and e3:
    cnt += 1

print(cnt)
