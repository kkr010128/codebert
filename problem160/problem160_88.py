N, M ,Q = map(int,input().split())

Rq = [list(map(int,input().split())) for _ in range(Q)]

ary = [1 for _ in range(N)]
ans = 0
while True:
  #print(ary)
  pt = 0
  for j in range(Q):
    rq = Rq[j]
    if ary[rq[1]-1]-ary[rq[0]-1] == rq[2]:
      pt += rq[3]
  ans = max(ans,pt)
  
  if ary[0] == M:
    break
  
  #次の配列へ
  for i in range(-1, -N-1, -1):
    if ary[i] < M:
      ary[i] += 1
      tmp = ary[i]
      for l in range(i+1, 0):
        ary[l] = tmp
      break
      
print(ans)
