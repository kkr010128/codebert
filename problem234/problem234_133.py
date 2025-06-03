import sys
input = sys.stdin.readline

n=int(input())
dp=[[0]*10 for _ in range(10)]

for i in range(1,n+1):
    dp[int(str(i)[0])][int(str(i)[-1])]+=1

#print(dp)
ans = 0
for i in range(10):
    for j in range(10):
        ans+=dp[i][j]*dp[j][i]
print(ans)
    
