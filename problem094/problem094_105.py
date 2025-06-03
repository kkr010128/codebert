import sys
input=sys.stdin.readline
def main():
    r,c,k=map(int,input().split())
    v=[0] * (c * r)
    for _ in range(k):
        ri,ci,a=map(int,input().split())
        v[(ri-1)*c + (ci-1)]=a
    dp= [0] * (c * r * 4)
    #print(dp)
    x = c * r
    if v[0]>0: dp[x] = v[0]

    for i in range(r):
        for j in range(c):
            idx = i*c+j
            idx2 = (i-1)*c + j
            idx3 = i*c + j-1
            if i>0:
                dp[x + idx] = max(dp[x + idx], dp[idx2]+v[idx])
                dp[idx] = max(dp[idx],dp[idx2])
                dp[x + idx]=max(dp[x + idx],dp[x + idx2]+v[idx])
                dp[idx]=max(dp[idx],dp[x + idx2])
                dp[x + idx]=max(dp[x + idx],dp[2*x + idx2]+v[idx])
                dp[idx]=max(dp[idx],dp[2*x + idx2])
                dp[x + idx]=max(dp[x + idx],dp[3*x + idx2]+v[idx])
                dp[idx]=max(dp[idx],dp[3*x + idx2])
            if j>0:
                dp[x + idx]=max(dp[x + idx],dp[idx3]+v[idx])
                dp[2*x + idx]=max(dp[2*x + idx],dp[x + idx3]+v[idx])
                dp[3*x + idx]=max(dp[3*x + idx],dp[2*x + idx3]+v[idx])
                dp[idx]=max(dp[idx],dp[idx3])
                dp[x + idx]=max(dp[x + idx],dp[x + idx3])
                dp[2*x + idx]=max(dp[2*x + idx],dp[2*x + idx3])
                dp[3*x + idx]=max(dp[3*x + idx],dp[3*x + idx3])

    #print(dp)
    ans=0
    for i in range(4): ans=max(dp[i*x + (r-1)*c + (c-1)],ans)
    return print(ans)

if __name__=="__main__":
    main()

