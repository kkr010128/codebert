n,p=map(int,input().split())
s=input()
if p==2 or p==5:
    ans=0
    for i in range(n):
        if int(s[i])%p==0:
            ans+=i+1
    print(ans)
else:
    t=[]
    ti=0
    for i in range(n):
        ti+=int(s[-i-1])*pow(10,i,p)
        ti%=p
        t.append(ti)
    from collections import Counter
    tc=Counter(t)
    ans=0
    for v in tc.values():
        ans+=(v*(v-1))//2
    if 0 in tc:
        ans+=tc[0]
    print(ans)
