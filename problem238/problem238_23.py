n,k,s=map(int,input().split())
ans=[s]*k
if n-k>0:
  ans1=[]
  if s==10**9:
    ans1=[1]*(n-k)
  else:
    ans1=[s+1]*(n-k)
  ans[len(ans):len(ans)]=ans1
print(' '.join(map(str,ans)))