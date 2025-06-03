def getval():
    h,n = map(int,input().split())
    m = [list(map(int,input().split())) for i in range(n)]
    return h,n,m

def main(h,n,m):
    #DP for minimal mp needed to do h damage
    dp = [0]
    for i in range(h):
        update = 2**60
        for j in m:
            if j[0]>=(i+1):
                update = min(update,j[1])
            else:
                update = min(update,j[1]+dp[i+1-j[0]])
        dp.append(update)
    print(dp[h])    
                
if __name__=="__main__":
    h,n,m = getval()
    main(h,n,m)