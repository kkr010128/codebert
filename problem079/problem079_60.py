INF=1000000000+7

s=int(input())
dp=[0]*(2000+1);
	
dp[0]=dp[1]=dp[2]=0
dp[3]=1


for i in range(4,s+1):
	temp=1
	for j in range(3,i-2):
		temp+=dp[j]%INF;
	temp%=INF;
	dp[i]=temp
print(dp[s])
