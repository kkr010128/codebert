a,b,m=map(int,input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
minimum=100000000000000
for i in range(m):
  x,y,z=map(int,input().split())
  minimum=min(minimum,alist[x-1]+blist[y-1]-z)
alist.sort()
blist.sort()
minimum=min(minimum,alist[0]+blist[0])
print(minimum)