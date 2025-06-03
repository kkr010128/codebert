S=input()
N=len(S)
K=int(input())
s="".join((S,S))
cnt1=0
cnt2=0
buf=0
piv=""
if len(set(S))!=1:
    for i in range(N):
        if S[i]==piv:
            buf=buf+1
        else:
            piv=S[i]
            cnt1=cnt1+(buf+1)//2
            buf=0
    cnt1=cnt1+(buf+1)//2
    buf=0
    piv=""
    for i in range(2*N):
        if s[i]==piv:
            buf=buf+1
        else:
            piv=s[i]
            cnt2=cnt2+(buf+1)//2
            buf=0
    #print(buf)
    cnt2 = cnt2 + (buf + 1) // 2
    x = cnt2 - cnt1
    print(cnt1 + (K - 1) * x)
else:
    print((len(S)*K)//2)
