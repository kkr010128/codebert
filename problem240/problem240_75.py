N,M=map(int,input().split()) 
L=[list(input().split()) for i in range(M)]
W=[0]*N
A=[0]*N
a=0
w=0
for i in range(M):
  if L[i][1]=="AC":
    A[int(L[i][0])-1]=1
    
  elif L[i][1]=="WA" and A[int(L[i][0])-1]==0:
    W[int(L[i][0])-1]+=1
#for i in A:
  #a+=i
#for i in W:
  #w+=i
for i in range(N):
  if A[i]>0:
    a+=1
    w+=W[i]
print(a,w)

