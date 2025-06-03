import sys
input=sys.stdin.readline

def main():
    r,c,k=map(int,input().split())

    item=[[0]*c for i in range(r)]
    for i in range(k):
        R,C,v=map(int,input().split())
        item[R-1][C-1]=v

    dp0=[[-10**10]*c  for i in range(r)]
    dp1 = [[-10 ** 10] * c for i in range(r)]
    dp2 = [[-10 ** 10] * c for i in range(r)]
    dp3 = [[-10 ** 10] * c for i in range(r)]

    if item[0][0]==0:
        dp0[0][0]=0
    else:
        dp0[0][0]=0
        dp1[0][0]=item[0][0]

    for i in range(r):
        for j in range(c):
            if j!=c-1:
                v=item[i][j+1]
                if v==0:
                    dp0[i][j+1]=max(dp0[i][j],dp0[i][j+1])
                    dp1[i][j + 1] = max(dp1[i][j], dp1[i][j + 1])
                    dp2[i][j + 1] = max(dp2[i][j], dp2[i][j + 1])
                    dp3[i][j + 1] = max(dp3[i][j], dp3[i][j + 1])
                else:
                    dp0[i][j+1]=max(dp0[i][j],dp0[i][j+1])
                    dp1[i][j+1]=max(dp0[i][j]+v,dp1[i][j],dp1[i][j+1])
                    dp2[i][j + 1] = max(dp1[i][j] + v, dp2[i][j], dp2[i][j + 1])
                    dp3[i][j + 1] = max(dp2[i][j] + v, dp3[i][j], dp3[i][j + 1])
            if i!=r-1:
                v=item[i+1][j]
                if v==0:
                    dp0[i+1][j]=max(dp0[i][j],dp1[i][j],dp2[i][j],dp3[i][j],dp0[i+1][j])
                else:
                    dp0[i+1][j]=max(dp0[i][j],dp1[i][j],dp2[i][j],dp3[i][j],dp0[i+1][j])
                    dp1[i + 1][j] = max(dp0[i][j]+v, dp1[i][j]+v, dp2[i][j]+v, dp3[i][j]+v, dp1[i + 1][j])

    ans=max(dp0[r-1][c-1],dp1[r-1][c-1],dp2[r-1][c-1],dp3[r-1][c-1])
    print(ans)

if __name__=='__main__':
    main()