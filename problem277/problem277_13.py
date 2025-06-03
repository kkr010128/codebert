h,w,k=map(int,input().split())
G=[["."]*w for i in range(h)]
for i in range(h):
  G[i]=list(input())
ans=[[0]*w for i in range(h)]
GG=[[0] for i in range(h)]
for i in range(h):
  for j in range(w):
    if G[i][j]=="#":
      GG[i].append(j)
  GG[i].append(w)
B=[0]
a=1
for i in range(h):
  if len(GG[i])==2:
    continue
  B.append(i)
  ans[i][GG[i][0]:GG[i][2]]=[a]*(GG[i][2]-GG[i][0])
  a=a+1
  for j in range(len(GG[i])-3):
    ans[i][GG[i][j+2]:GG[i][j+3]]=[a]*(GG[i][j+3]-GG[i][j+2])
    a=a+1
B.append(h)
for i in range(B[2]-B[0]):
  ans[i]=ans[B[1]]
for i in range(B[2],h):
  if i not in B:
    ans[i]=ans[i-1]
for i in range(h):
  for j in range(w):
    print(ans[i][j],end=" ")
  print()