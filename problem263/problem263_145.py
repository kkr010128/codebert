mod = pow(10, 9) + 7
N = int(input())
# 制約が a<2**60 なので
L = 60

A = map(int, input().split())

counter = [0] * L
for a in A:
    for i in range(L):
        counter[i] += a & 1
        a >>= 1

tmp = 0
for i in range(L):
    tmp += counter[i] * (N - counter[i]) * (2 ** i)
    tmp %= mod

print(tmp)
