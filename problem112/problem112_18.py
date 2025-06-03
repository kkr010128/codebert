n,k=map(int, input().split())
a = list(map(int, input().split()))
mod=10**9+7
if n==k:
    ans=1
    for i in range(k):
        ans*=a[i]
        ans%=mod
    print(ans)
    exit()
minus=[i for i in a if i<0]
plus=[i for i in a if i>=0]
from collections import deque
minus=deque(sorted(minus))
plus=deque(sorted(plus,reverse=True))

n_minus=len(minus)
n_plus=len(plus)

if n_minus==n:
    ans=1
    if k%2==0:
        for i in range(k):
            ans*=minus.popleft()
            ans+=mod
            ans%=mod
        print(ans)
        exit()
    else:
        for i in range(k):
            ans*=minus.pop()
            ans+=mod
            ans%=mod
        print(ans)
        exit()

cnt_minus=0
cand=deque([])
for i in range(k):
    if not plus or ((plus and minus) and abs(minus[0])>abs(plus[0])):
        cand.append(minus.popleft())
        cnt_minus+=1
    elif not minus or ((plus and minus) and abs(minus[0])<abs(plus[0])):
        cand.append(plus.popleft())
    else:
        if cnt_minus%2==1:
            cand.append(minus.popleft())
            cnt_minus+=1
        else:
            cand.append(plus.popleft())

if cnt_minus%2==0:
    ans=1
    for i in range(k):
        ans*=cand[i]
        ans+=mod
        ans%=mod
    print(ans)
    exit()

if 0 in cand:
    print(0)
    exit()

tmpm,tmpp=None,None

for i in range(k-1,-1,-1):
    if cand[i]<0 and tmpm==None:
        tmpm=cand[i]
    elif cand[i]>=0 and tmpp==None:
        tmpp=cand[i]

#print(tmpm,tmpp)
cand1,cand2=None,None
if tmpm!=None and plus:
    cand1=plus[0]/abs(tmpm)
if tmpp!=None and minus:
    if tmpp!=0:
        cand2=abs(minus[0])/abs(tmpp)
    else:
        cand2=0

if tmpp==0:
    if minus:
        ans=1
        flg=True
        for i in range(k):
            if flg and cand[i]==tmpp:
                flg=False
                continue
            ans*=cand[i]
            ans+=mod
            ans%=mod
        print((ans*minus[0])%mod)
        exit()
elif (cand1!=None and cand2==None) or ((cand1!=None and cand2!=None) and plus[0]*abs(tmpp)>=abs(minus[0]*tmpm)):
    ans=1
    flg=True
    for i in range(k):
        if flg and cand[i]==tmpm:
            flg=False
            continue
        ans*=cand[i]
        ans+=mod
        ans%=mod
    print((ans*plus[0])%mod)
    exit()

elif (cand1==None and cand2!=None) or ((cand1!=None and cand2!=None) and plus[0]*abs(tmpp)<abs(minus[0]*tmpm)):
    ans=1
    flg=True
    for i in range(k):
        if flg and cand[i]==tmpp:
            flg=False
            continue
        ans*=cand[i]
        ans+=mod
        ans%=mod
    print((ans*minus[0])%mod)
    exit()