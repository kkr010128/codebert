h,w,k=map(int,input().split())
s=[input() for _ in range(h)]
ans=[]
c=1
for si in s:
  ans.append([c]*w)
  c+=si.count('#')
ans.append([c]*w)
p=0
q=1
while q<=h:
  if ans[q][0]-ans[p][0]>=1:
    c=ans[p][0]
    for j in range(w):
      for i in range(p,q):
        ans[i][j]=c
        if s[i][j]=='#':
          c=min(c+1,ans[q][0]-1)
    p=q
    if ans[q-1][-1]==k:
      while q<h:
        ans[q]=ans[q-1]
        q+=1
  q+=1
for a in ans[:-1]:
  print(*a)