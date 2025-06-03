from heapq import heapify,heappush,heappop
N, M = map(int, input().split())

I = [[] for _ in range(N)]
for i in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  I[A].append(B)
  I[B].append(A)

task = [] 
used = [0 for _ in range(N)]
min_len = [0 for _ in range(N)]
length = [10**20 for _ in range(N)]
prev_points = [0 for _ in range(N)]
heappush(task, (0, 0, -1))
print("Yes")

while task:
  while task:
    l, p, prev = heappop(task)    
    if used[p] == 0:
      break
  #print(task)
  used[p] = 1
  min_len[p] = l
  prev_points[p] = prev +1 #番号を1ずらす
  
  for j in I[p]:
    if used[j] == 1: continue
    #print(p,j)
    if length[j] > l+1:
      length[j] = l+1
      heappush(task, (l+1, j, p))
    
for i in range(1, N):
  print(prev_points[i])