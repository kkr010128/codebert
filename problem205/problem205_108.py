N,P=map(int,input().split())
S=input()
s=[0 for i in range(N+1)]
a=[0 for i in range(N+1)]
a[0]=(10**0)%P
for i in range(N):
    A=a[i]
    a[i+1]=(A*(10%P))%P
    s[i+1]=(s[i]+A*int(S[N-i-1]))%P
d=[0 for i in range(P)]
for i in range(len(s)):
    d[s[i]]+=1
ans=0
if P!=2 and P!=5:
    for D in d:
        ans+=D*(D-1)//2
    print(ans)
elif P==2:
    for i in range(N):
        if int(S[N-1-i])%2==0:
            ans+=(N-i)
    print(ans)
else:
    for i in range(N):
        if int(S[N-1-i])%5==0:
            ans+=(N-i)
    print(ans)