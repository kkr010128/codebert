def solve(n,A):
    x=pow(2,n)
    dp=[False]*2001
    for i in range(x):
        count=0
        for j in range(n):
            if (i>>j)&1:
                count+=A[j]
        if count<=2000:
            dp[count]=True
    return dp

n=int(input())
A=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))
ans=solve(n,A)
for i in range(q):
    if ans[m[i]]:
        print("yes")
    else:
        print("no")
