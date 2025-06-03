N=int(input())
XL=[]
for _ in range(N):
    a=list(map(int,input().split()))
    XL.append(a)
XL = sorted(XL, key=lambda x:x[0]+x[1])
#前から順に取っていく
#DP[i]:i番目までのロボットで残せるロボットの最大数
#i番目のロボットがどこまでをカバーしているかを格納する必要がある
DP=[[0,0] for i in range(N)]
DP[0][0]=1#個数
DP[0][1]=XL[0][0]+XL[0][1]#カバーしている距離
for i in range(1,N):
    if XL[i][0]-XL[i][1]>=DP[i-1][1]:
        DP[i][0]=DP[i-1][0]+1
        DP[i][1]=XL[i][0]+XL[i][1]
    else:
        DP[i][0]=DP[i-1][0]
        DP[i][1]=DP[i-1][1]
print(DP[-1][0])