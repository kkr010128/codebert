n=int(input())
dp=[0]*(n+1)
dp[0]=1
dp[1]=1


def rec(x):
    if dp[x]>0:
        return dp[x]

    res=rec(x-1)+rec(x-2)
    dp[x]=res
    return dp[x]

print(rec(n))

