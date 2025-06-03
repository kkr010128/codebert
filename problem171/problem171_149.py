#active infants

n=int(input())
lists=list(map(int,input().split()))
data=[]
for i in range(n):
    data.append((lists[i],i+1))
data=sorted(data,key=lambda x:-x[0])


#dp[K][i]=始めのKつまで考えてそのうちプラスの個数がiこの方法で最大のあたい(0<=i<=K)
#求める値はmax(dp[N][i]　for i in range(N+1))で与えられる
#dp[N][N]まで考えればいい

#計算量0(N**2)
dp=[[0 for i in range(n+1)] for j in range(n+1)]

dp[1][1]=n*(data[0][0])-data[0][0]*data[0][1]
dp[1][0]=data[0][0]*data[0][1]-data[0][0]

for i in range(2,n+1):
    #dp[i]について考える
    for j in range(i+1):
        x=data[i-1][0]
        y=data[i-1][1]
        #j=0,1,,,,,iまで
        #dp[i][j]-> 直前は i-1,j-1, or i-1 j のどちらか
        if i>j>=1:
            dp[i][j]=max(dp[i-1][j-1]+x*(n+1-j)-x*y,dp[i-1][j]-(i-j)*x+x*y)
        elif j==0:
            dp[i][j]=dp[i-1][0]-i*x+x*y
        elif j==i:
            dp[i][j]=dp[i-1][i-1]+x*(n+1-j)-x*y        
K=0
for i in range(n+1):
    K=max(K,dp[n][i])
print(K)



