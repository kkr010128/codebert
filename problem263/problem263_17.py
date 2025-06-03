import math

N = int(input())
A = list(map(int, input().split()))

Sum = 0
mod = (10 ** 9) + 7

for i in range(len(bin(max(A)))-2):
    Sum_1 = 0
    for j in range(N):
        #print(i, j)
        if ((A[j] >> i) & 1):
            Sum_1 += 1

    Sum_0 = N - Sum_1

    Sum = (Sum + ((Sum_0 * Sum_1) % mod * (2 ** i)) % mod) % mod
    # print(Sum_0,Sum_1)

print(Sum)
