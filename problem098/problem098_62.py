n=int(input())
s=input()
A=[]
for i in range(n):
  A.append(s[i])
W=0
R=A.count('R')
ans=float('inf')
for i in range(n+1):
  if i!=0:
    if A[i-1]=='W':
      W+=1
    else:
      R-=1
  ans=min(max(W,R),ans)
print(ans)