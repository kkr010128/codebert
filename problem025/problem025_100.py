import bisect
n = int(input())
A = tuple(map(int,input().split()))
q = int(input())
Q = tuple(map(int, input().split()))
dp = [0]*(2**n)

for i in range(n):
    for j in range(1<<i):
        dp[j+(1<<i)] = dp[j] + A[i]
dp.sort()

for n in Q:
    i = bisect.bisect(dp, n)
    print("yes" if i>0 and n==dp[i-1] else "no")