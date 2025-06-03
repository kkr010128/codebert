import sys
import math

n, k = map(int, input().split())

# n_start = math.floor(n / k)
# # print(n_start)
# n = n - n_start*k
# # print(n)

n = n % k

while True:
    min_n = n
    n = abs(n-k)
    # print("n, k =", n, k)
    if min_n > n:
        min_n = n
    else:
        break
print(min_n)
