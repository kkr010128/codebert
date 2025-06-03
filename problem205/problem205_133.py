from collections import defaultdict
dd = defaultdict(int)
n,p=map(int, input().split())
S = list(input().rstrip())
tmp = 0
r=1
su=0
dd[0]=1
if p==2 or p==5:
    c=n
    for s in S[::-1]:
        if int(s)%p==0:
            su+=c
        c-=1
    print(su)
else:
    for s in S[::-1]:
        tmp+=int(s)*r
        tmp%=p
        dd[tmp]+=1
        r*=10
        r%=p
    for i in dd.values():
        su += (i*(i-1))//2
    print(su)
