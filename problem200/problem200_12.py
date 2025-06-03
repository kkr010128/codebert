a,b,m=map(int,input().split())
aa=list(map(int,input().split()))
bb=list(map(int,input().split()))

lst=[]
for i in range(m):
  x,y,z=list(map(int,input().split()))
  lst.append([x,y,z])
  
ans=min(aa)+min(bb)

for i in lst:
  ans=min(ans,aa[i[0]-1]+bb[i[1]-1]-i[2])
  
  
print(ans)