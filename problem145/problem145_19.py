N, M = map(int, input().split())
nextroom = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  nextroom[A-1].append(B-1)
  nextroom[B-1].append(A-1)

sgn = [-1 for _ in range(N)]
sgn[0] = 0

depth = [float('inf') for _ in range(N)]
depth[0] = 0

now = [0]
nextvisit = []
for j in range(1, M+1):
  for n in now:
    for i in nextroom[n]: 
      if depth[i] > j:
        nextvisit.append(i)
        sgn[i] = n
        depth[i] = j
  now = [] + nextvisit
  nextvisit = []

if -1 in sgn:
  print('No')
else:
  print('Yes')
  for k in range(1, len(sgn)):
    print(sgn[k]+1)