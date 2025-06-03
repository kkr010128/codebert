import sys
input = sys.stdin.readline 
N=int(input())
L=list(map(int,input().split()))
Q=int(input())
R=[0]*(10**5)
for i in L:
  R[i-1]+=1
ans=sum(L)
for i in range(Q):
  a,b=map(int,input().split())
  R[b-1]+=R[a-1]
  ans+=(b-a)*R[a-1]
  R[a-1]=0
  print(ans)