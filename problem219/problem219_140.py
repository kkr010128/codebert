def dp_solver(tmp):
    l=len(tmp)
    rev=tmp[::-1]+"0"
    dp=[[float("inf") for _ in range(2)] for _ in range(l+2)]
    dp[0][0]=0
    for i in range(l+1):
        for j in range(2):
            num=int(rev[i])
            num+=j
            if num<10:
                dp[i+1][0]=min(dp[i+1][0],dp[i][j]+num)
            if num>0:
                dp[i+1][1]=min(dp[i+1][1],dp[i][j]+(10-num))

    #import numpy as np
    #dp=np.array(dp)
    return(dp[l+1])

s=input()
ans=dp_solver(s)
print(ans[0])