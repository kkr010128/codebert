from  bisect import bisect

n,d,a=map(int,input().split())
monster=[list(map(int,input().split())) for i in range(n)]
monster.sort(key=lambda i:i[0])
r=[monster[i][0] for i in range(n)]
hp=[monster[i][1] for i  in range(n)]
#print(r,hp)

d=2*d
i,ans,damages=0,0,[0]*n
while i<n:
  if i>0:
    damages[i]+=damages[i-1]
    s=hp[i]+damages[i]
  else:
    s=hp[i]
  if s>0:
    cnt=(s+a-1)//a
    ans+=cnt
    #print(ans)
    damage=cnt*a
    damages[i]-=damage
    zone=bisect(r,r[i]+d)
    if zone<n:
      damages[zone]+=damage 
  i+=1
  #print(damages)
  #print(hp)
print(ans)
