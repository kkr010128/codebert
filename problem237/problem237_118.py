N=int(input())

rllist=[]
for _ in range(N):
  X,L=map(int,input().split())
  rllist.append((X+L,X-L))
rllist.sort()
#print(rllist)

answer=0
max_r=-float("inf")
for r,l in rllist:
  #print(max_r,l)
  if max_r<=l:
    answer+=1
    max_r=r
  
print(answer)