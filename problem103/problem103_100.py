N=int(input())
A=list(map(int,input().split()))
M=1000
S=0

for i in range(N-1):
  if A[i+1]>A[i]:
    S+=M//A[i]
    M-=A[i]*(M//A[i])
  else:
    M+=S*A[i]
    S=0
    
print(M+S*A[N-1])