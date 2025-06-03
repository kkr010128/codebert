N=input()
L=len(N)
ans=[[0 for e in range(2)] for f in range(L)]
ans[0][0]=int(N[L-1])
ans[0][1]=10-int(N[L-1])
if L>1:
 for i in range(1,L):
  ans[i][0]=min(ans[i-1][0]+int(N[L-1-i]),ans[i-1][1]+int(N[L-1-i])+1)
  ans[i][1]=min(ans[i-1][0]+10-int(N[L-1-i]),ans[i-1][1]+10-int(N[L-1-i])-1)
print(min(ans[L-1][0],ans[L-1][1]+1))