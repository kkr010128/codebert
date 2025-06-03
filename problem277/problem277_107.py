h,w,k=map(int,input().split())
b=[input()for _ in range(h)]
ans=[w*[0]for _ in range(h)]
f=[1]*h
j=-1
bb=[]
for i in range(h):
  if "#"in b[i]:
    f[i]=0
    j=i
    if len(bb)==0:continue
    for k in bb:ans[k]=ans[j]
    bb=[]
  else:
    if j<0:bb.append(i)
    else:ans[i]=ans[j]
a=1
for i in range(h):
  if f[i]:continue
  fl=False
  for j in range(w):
    if b[i][j]=="#":
      if fl:a+=1
      fl=True
    ans[i][j]=a
  if fl:a+=1
for i in ans:print(*i)