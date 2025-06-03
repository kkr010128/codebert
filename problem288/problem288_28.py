import math
n = int(input())
#探索範囲
sqrt_n = int(math.sqrt(n))
num_i = 0
for i in range(1, sqrt_n+1):
    if n % i == 0:
       num_i = i

num_j = n // num_i
ans = (num_i - 1) + (num_j - 1)

print(ans)

