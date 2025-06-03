import itertools

n,m,q=map(int,input().split())
lst=[]
ans=0

for i in range(q):
  a,b,c,d=map(int,input().split())
  lst.append([a,b,c,d])

for x in list(itertools.combinations_with_replacement(range(1,m+1),n)):
  cnt=0
  for i in lst:
    if x[i[1]-1]-x[i[0]-1]==i[2]:
      cnt+=i[3]

  ans=max(ans,cnt)


print(ans)