n=int(input())
s=[0]*n
info=[0]*n
for i in range(n):
    ss=list(input())
    now=0
    mi=0
    for sss in ss:
        if sss=="(":
            now+=1
        else:
            now-=1
            mi=min(mi,now)
    info[i]=(mi,now)
#info.sort(key=lambda x:(x[1]>=0)*2+(x[0]>=0),reverse=True )

info0 = []
info1 = []
for i,inf in enumerate(info):
    if inf[1]>=0:
        info0.append(inf)
    else:
        info1.append(inf)
info0.sort(key=lambda x:x[0],reverse=True)
info1.sort(key=lambda x:x[1]-x[0],reverse=True)


ans=True
now=0
for inf in info0:
    if now+inf[0]>=0:
        now+=inf[1]
    else:
        ans=False
for inf in info1:
    if now+inf[0]>=0:
        now+=inf[1]
    else:
        ans=False
if now!=0:
    ans=False
    
print(ans*"Yes"+(1-ans)*"No")