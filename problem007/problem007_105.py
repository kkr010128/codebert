N=int(input())
DP=[]
DP.append(1)
DP.append(1)
for i in range(2,N+1):
    DP.append(DP[i-1]+DP[i-2])
print(DP[N])
