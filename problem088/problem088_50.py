def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

N=II()
A=LI()
L=[0]*N
TM=A[0]
for i in range(N):
  TM=max(TM,A[i])
  L[i]=TM-A[i]
  
  #print(L[i],TM,A[i])
ans=sum(L)
print(ans)