S = int(input())
MOD = 10 ** 9 + 7

DP = [0] * (2000+1)
DP[0]
 
DP[3]=1
for i in range(4,2001):
    DP[i]=DP[i-1]+DP[i-3]

print(DP[S]%(10**9+7))  