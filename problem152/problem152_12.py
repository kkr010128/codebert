n=int(input())
s=[input() for _ in range(n)]
d0={}
d1={}
ma=0
mab=0
for si in s:
    a,b=0,0
    for x in si:
        if x=='(':
            b+=1
        else:
            b-=1
        a=min(b,a)
    a=-a
    if b>=0:
        if a in d0:
            d0[a].append([a,b])
        else:
            d0[a]=[[a,b]]
        ma=max(ma,a)
    else:
        if a+b in d1:
            d1[a+b].append([a,b])
        else:
            d1[a+b]=[[a,b]]
        mab=max(mab,a+b)
now=0
for i in range(ma+1):
    if i not in d0:continue
    if now>=i:
        for a,b in d0[i]:
            now+=b
    else:
        print('No')
        exit()
for i in range(mab,-1,-1):
    if i not in d1:continue
    for a,b in d1[i]:
        if now>=a:
            now+=b
        else:
            print('No')
            exit()
if now==0:
    print('Yes')
else:
    print('No')