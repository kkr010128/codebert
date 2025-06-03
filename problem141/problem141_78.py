n=int(input())
a=list(map(int,input().split()))
if n==0:
  if a[0]==1:
    print(1)
    exit()
  else:
    print(-1)
    exit()
if a[0]>0:
  print(-1)
  exit()

ans=1
pre_no_ha=1
all_ha=sum(a)

for ai in a[1:]:
  if pre_no_ha<=0:
    print(-1)
    exit()
  if ai>pre_no_ha*2:
    print(-1)
    exit()
  
  pre_no_ha*=2
  pre_no_ha-=ai
  all_ha-=ai
  pre_no_ha=min(pre_no_ha,all_ha)
  ans+=pre_no_ha+ai

print(ans)