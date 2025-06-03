N,M,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_s=[0]
b_s=[0]
for i in range(N):
  if a_s[i]+a[i]>K:
    break
  a_s.append(a[i]+a_s[i])
for i in range(M):
  if b_s[i]+b[i]>K:
    break
  b_s.append(b[i]+b_s[i])
bn=len(b_s)-1
ans=0
for i in range(len(a_s)):
  while a_s[i]+b_s[bn]>K:
    bn-=1
  ans=max(ans,i+bn)
  
print(ans)