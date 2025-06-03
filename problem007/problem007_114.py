N=int(input())
DP=[0]*(N+1)
def fin(n):
    if DP[n]!=0:
        return DP[n]
    if n<=1:
        DP[n]=1
        return DP[n]
    else:
        DP[n]=fin(n-1)+fin(n-2)
        return DP[n]
print(fin(N))
