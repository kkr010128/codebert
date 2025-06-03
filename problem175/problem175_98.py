n=int(input())
s=input()
R=[]
G={}
B=[]
for i in range(n):
  if s[i]=='R':
    R.append(i+1)
  elif s[i]=='G':
    G[i+1]=G.get(i+1,0)+1
  else:
    B.append(i+1)
res=len(R)*len(G)*len(B)
for i in R:
  for j in B:
    if ((i+j)%2==0 and G.get((i+j)//2,0)==1):
      res-=1
    if G.get(2*max(i,j)-min(i,j),0)==1:
      res-=1
    if G.get(2*min(i,j)-max(i,j),0)==1:
      res-=1
print(res)