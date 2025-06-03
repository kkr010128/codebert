# coding: utf-8
import math
#n, k, s = map(int,input().split())
n = int(input())
A = list(map(int,input().split()))
ans = 0
MOD=10**9+7
L0 = [0] * 60
L1 = [0] * 60
for i in range(n):
    b = A[i]
    #print(b)
    b = format(b, '060b')
    #print(b)
    for j in range(60):
        if b[60 - j  -1] == "1":
            L1[j] += 1
        else:
            L0[j] += 1
#print(L0)
#print(L1)

for i in range(60):
    ans += L0[i] * L1[i] * 2**i
    ans %= MOD
print(ans)