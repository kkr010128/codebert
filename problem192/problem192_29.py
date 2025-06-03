import collections
import itertools

N = int(input())
A = list(map(int, input().split()))

ac = collections.Counter(A)

dp = [0] * (N+1)
dp2 = [0] * (N+1)
total = 0
for no, num in ac.items():
    dp[no] = int(num*(num-1)/2)
    dp2[no] = dp[no] - (num-1)
    total += dp[no]

for k in range(1,N+1):
    no = A[k-1]
    print(int(total - dp[no] + dp2[no]))
