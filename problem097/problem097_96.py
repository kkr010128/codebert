K=int(input())
A=0
for i in range(K):
  A=(A*10+7)%K
  if A%K==0:
    print(i+1)
    break
  if i==K-1:print(-1)