B=[];C=[];S=0
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
for i in range(Q):
  b,c=map(int,input().split())
  B.append(b)
  C.append(c)

X=[0]*(10**5+1)
for i in range(N):
  X[A[i]]+=1
  S=S+A[i]

#print(A)
#print(B)
#print(C)

for i in range(Q):
  X[C[i]]+=X[B[i]]
  S=S+X[B[i]]*(C[i]-B[i])
  X[B[i]]=0
  print(S)