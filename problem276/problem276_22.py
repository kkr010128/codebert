N=int(input())
alist=list(map(int,input().split()))

slist=[0]
for a in alist:
  slist.append(slist[-1]+a)  
#print(slist)

answer=float("inf")
for i in range(N+1):
  s1=slist[i]
  s2=slist[-1]-s1
  answer=min(answer,abs(s1-s2))
  
print(answer)