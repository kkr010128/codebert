A,B,R=list(map(int,input().split()))
K=B+R
ans=B*(A//K)
S=A%K
if S<=B:
  ans+=S
else:
  ans+=B
print(ans)