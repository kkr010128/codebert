n=int(input())
if n%2==1:
    print(0)
else:
    ans=0
    k=10
    while k<=n:
        t=n//k
        ans+=t
        k*=5
    print(ans)