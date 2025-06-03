from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    dp=[0]*(n+1)
    for i in range(n+1):
        if i==0 or i==1:
            dp[i]=1
        else:
            dp[i]=dp[i-1]+dp[i-2]

    print(dp[n])
    
if __name__=="__main__":
    main()
