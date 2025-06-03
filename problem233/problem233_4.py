n=int(input())
p=list(map(int,input().split()))

ans=0

min_=p[0]

for pp in p:
  min_=min(min_,pp)
  if min_ ==pp:
    ans+=1

print(ans)