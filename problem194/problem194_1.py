import numpy as np

H,W = input().split()
H,W=int(H),int(W)
P=[0]*H
for i in range(H):
    P[i] = input()

dp=np.zeros((H,W),dtype='u8')
if P[0][0]=='#':
    dp[0][0]=1
else:
    dp[0][0]=0

def DP(y,x):
    global dp
    if 0<=x<=W-1 and 0<=y<=H-1:
        return dp[y][x]
    else:
        return 9999999

for l in range(1,H+W):
    for i in range(l+1):
        if i<H and l-i<W:
            if P[i][l-i]=='#':
                a=DP(i-1,l-i)
                b=DP(i,l-i-1)
                if a < 9999999:
                    if P[i-1][l-i]=='.':
                        a+=1
                if b <  9999999:
                    if P[i][l-i-1]=='.':
                        b+=1
                dp[i][l-i]=min(a,b)
            else:
                #print(i,l-i,DP(i-1,l-i),DP(i,l-i-1))
                dp[i][l-i]=min(DP(i-1,l-i),DP(i,l-i-1))
print(dp[H-1][W-1])