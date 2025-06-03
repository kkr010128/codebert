h,w,k=[int(j) for j in input().split()]
s=[list(map(int,list(input()))) for i in range(h)]
import itertools
s=tuple(itertools.chain(*zip(*s)))
ans=10**18
for i in range(1<<(h-1)):
    dp=list(s)
    for j in range(h-1):
        if i&(1<<j):
            for n in range(0,h*w,h):
                dp[n+j+1]+=dp[n+j]
    tmp=h-1-bin(i).count("1")
    b=False
    for n in range(0,h*w,h):
        if any(dp[n+j]>k for j in range(h)):
            tmp=10**18
            break
        if n+h==h*w:
            ans=min(ans,tmp)
            tmp=10**18
            break
        if any(dp[n+j]+dp[n+j+h]>k for j in range(h)):
            tmp+=1
            continue
        for j in range(h):
            dp[n+j+h]+=dp[n+j]
    ans=min(ans,tmp)
print(ans)