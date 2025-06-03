A,B,M=map(int,input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
 
answer=min(alist)+min(blist)
for _ in range(M):
  x,y,c=map(int,input().split())
  disc=alist[x-1]+blist[y-1]-c
  answer=min(answer,disc)
  
print(answer)