# Sum of Divisors
import math

N = int(input())
ans = 0

for i in range(1,N+1):
    K = math.floor(N/i)
    ans += (K * (K+1) * i)/2

print(int(ans))

