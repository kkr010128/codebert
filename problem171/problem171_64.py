def main():
    n=int(input())
    A=list(zip(list(map(int,input().split())),range(n)))
    A.sort(reverse=True)
    DP=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i+j>n:
                break
            a,idx=A[i+j-1]
            if i>0:
                DP[i][j]=max(DP[i][j],DP[i-1][j]+a*abs(idx-(i-1)))
            if j>0:
                DP[i][j]=max(DP[i][j],DP[i][j-1]+a*abs(idx-(n-j)))
    ans=0
    for i in range(n+1):
        ans=max(ans,DP[i][n-i])
    print(ans)
    
if __name__=='__main__':
    main()