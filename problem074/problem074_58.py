def main():
    mod=998244353
    n,k=map(int,input().split())
    region=[]
    for _ in range(k):
        a,b=map(int,input().split())
        region.append((a,b))

    #dp[i]はマスiに行く方法の個数
    #workにdp[i-1]からの増減分を保持
    dp=[0]*(n+1)
    work=[0]*(n+1)

    #initialize
    for j in region:
        if 1+j[0]<=n:
            work[1+j[0]]+=1
        if 1+j[1]+1<=n:
            work[1+j[1]+1]-=1    

    for i in range(2,n+1):
        dp[i]=dp[i-1]+work[i]
        dp[i]%=mod
        for j in region:
            if i+j[0]<=n:
                work[i+j[0]]+=dp[i]
                work[i+j[0]]%=mod
            if i+j[1]+1<=n:
                work[i+j[1]+1]-=dp[i]
                work[i+j[1]+1]%=mod
    print(dp[n])


main()