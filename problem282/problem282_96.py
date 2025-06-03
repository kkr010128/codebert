import sys
def input(): return sys.stdin.readline().rstrip()
 
def main():
    n,t=map(int, input().split())
    dp=[0]*t
    food=[]
    for _ in range(n):
        a,b=map(int, input().split())
        food.append([a,b])
    food.sort(key=lambda x:x[0]*-1)
    for j in range(n):
        a,b=food[j][0],food[j][1]
        dptmp=[0]*t
        for i in range(t):
            if i < a: 
                dptmp[i]=max(b,dp[i])
            else:
                dptmp[i]=max(dp[i-a]+b,dp[i])
        dp=dptmp
    print(dp[t-1])
 
if __name__=='__main__':
    main()