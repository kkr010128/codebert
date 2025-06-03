N, K = map(int,input().split())
A = list(map(int,input().split()))
B = [0];BB=[0]
S = set([]);S.add(0)
now = 0
Flag = False
loop_start = -1
if K <= 2*pow(10,5)+10:
  for i in range(K):
    nxt = A[now]-1
    BB.append(nxt)
    now = nxt
  #print(BB)
  print(BB[K]+1)
  exit()
for i in range(N*2):
  nxt = A[now]-1
  #print(now,nxt)
  if nxt in S:
    if Flag:
      if nxt == loop_start:
        #print(nxt,i)
        loop_cycle = i-loop_num
        break
    else:
      loop_start = nxt
      loop_num = i
      B.append(nxt)
      #print(loop_num,loop_start,B)
      Flag = True
  else:
    B.append(nxt);S.add(nxt)
  now = nxt
loop_num += 1-loop_cycle
#print(B,loop_start,loop_cycle,loop_num)
loc = (K-loop_num)%loop_cycle+loop_num
#print(loc)
#print(len(B))
print(B[loc]+1)