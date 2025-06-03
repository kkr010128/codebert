h,w=map(int,input().split())
s=['*'+'.'+'*'*w]+['*'+input()+'*' for i in range(h)]+['*'*(w+2)]
b=10**9
d=[[b]*(w+2)]+[[b]+[0]*w+[b] for _ in range(h)]+[[b]*(w+2)]
d[0][1]=0
for i in range(1,h+1):
  for j in range(1,w+1):
    d[i][j]=min(d[i-1][j]+(s[i][j]=='#')*(s[i-1][j]=='.'),d[i][j-1]+(s[i][j]=='#')*(s[i][j-1]=='.'))
print(d[h][w])