def main():
    import sys
    input=sys.stdin.readline
    n=int(input())
    A=list(map(int,input().split()))
    A_=[]
    for i in range(n):
        A_.append([A[i],i])
    A_sorted=sorted(A_)[::-1]
    dp=[[0]*(n+1) for _ in range(n+1)]
    ans=0
    for xy in range(1,n+1):
        for x in range(xy+1):
            m=-float("INF")
            a=A_sorted[xy-1][0]
            a_i=A_sorted[xy-1][1]
            if x!=0 and x<=a_i+1:
                m=max(m,dp[x-1][xy-x]+a*(a_i+1-x))
            if x!=xy and n-xy+x>=a_i:
                m=max(m,dp[x][xy-x-1]+a*(n-xy+x-a_i))
            dp[x][xy-x]=m
            if xy==n:
                ans=max(ans,m)
    print(ans)
if __name__ == '__main__':
    main()