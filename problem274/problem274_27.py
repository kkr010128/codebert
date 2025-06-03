import sys
input = sys.stdin.readline
N,M=map(int,input().split());S=input()[:-1]
if S.find("1"*M)>0:
  print(-1)
  exit()
k=[N+1]*(N+1)
k[0]=N
c=1
for i in range(N-1,-1,-1):
  if int(S[i])==0:
    if k[c-1]-i <= M:
      k[c]=i
    else:
      c+=1
      k[c]=i

print(*[j-i for i,j in zip(k[c::-1],k[c-1::-1])])