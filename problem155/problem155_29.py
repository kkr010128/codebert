n,m=map(int,input().split())
H=list(map(int,input().split()))
ans = [1]*n
for i in range(m):
  a,b=map(int,input().split())
  if H[a-1]>H[b-1]:
    ans[a-1] *= 1 
    ans[b-1] *= 0
  elif H[a-1]<H[b-1]:
    ans[a-1] *= 0
    ans[b-1] *= 1
  else:
    ans[a-1] *= 0
    ans[b-1] *= 0
print(sum(ans))