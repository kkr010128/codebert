h,w=map(int,input().split())
field=[list(input()) for i in range(h)]
ans=[[0 for i in range(w)]for j in range(h)]
if field[0][0]=='#':
  ans[0][0]=1

def black(i,j,f):
  if f==1:
    if field[i][j]=='#' and field[i-1][j]=='.':
      return 1
    else:
      return 0
  else:
    if field[i][j]=='#' and field[i][j-1]=='.':
      return 1
    else:
      return 0
for i in range(h):
  for j in range(w):
    if i==0 and j==0:
      continue
    elif i==0:
      ans[i][j]=ans[i][j-1]+black(i,j,2)
    elif j==0:
      ans[i][j]=ans[i-1][j]+black(i,j,1)
    else:
      ans[i][j]=min(ans[i-1][j]+black(i,j,1),ans[i][j-1]+black(i,j,2))
print(ans[-1][-1])