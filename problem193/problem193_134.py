from itertools import accumulate
h,w,k=map(int,input().split())
s=[[0]*(w+1)]+[[0]+[int(i) for i in input()] for _ in range(h)]
for i in range(h+1):
  s[i]=list(accumulate(s[i]))
for j in range(w+1):
  for i in range(h):
    s[i+1][j]+=s[i][j]
ans=10**18
for i in range(1<<h-1):
  a=[]
  for j in range(h-1):
    if (i>>j)&1:a+=[j+1]
  a+=[h]
  cnt=len(a)-1
  q=1
  for j in range(1,w+1):
    p=0
    flag=0
    for l in a:
      if s[l][j]-s[l][j-1]-s[p][j]+s[p][j-1]>k:flag=1
      elif s[l][j]-s[l][q-1]-s[p][j]+s[p][q-1]>k:
        q=j
        cnt+=1
        break
      else:p=l
    if flag:break
  else:
    ans=min(cnt,ans)
print(ans)