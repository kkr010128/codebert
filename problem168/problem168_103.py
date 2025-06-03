n,m=map(int,input().split())
a=list(map(int,input().split()))

ans=0
for i in range(m) :
    ans = ans+a[i]

day=n-ans

#if day>=0 :
#    print(day)
#else :
#    print(-1)

print(day if day >= 0 else "-1")