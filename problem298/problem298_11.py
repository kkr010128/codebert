N,K=map(int,input().split())
H=list(map(int,input().split()))
P=0
for i in range(N):
  if K<=H[i]:
    P+=1
print(P)