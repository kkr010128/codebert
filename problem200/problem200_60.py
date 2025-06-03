A,B,M=map(int,input().split())
aa=list(map(int,input().split()))
bb=list(map(int,input().split()))
XC=[]
for i in range(M):
  XC.append(list(map(int,input().split())))
ans=min(aa)+min(bb)
for i in range(M):
  ans=min(ans,aa[XC[i][0]-1]+bb[XC[i][1]-1]-XC[i][2])
print(ans)