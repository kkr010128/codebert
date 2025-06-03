from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

mod = 10**9 + 7
memo = defaultdict(int)
base = 0
for i in a:
    base = (base+pow(i, mod-2, mod))%mod
    num = i
    for j in range(2, int(i**.5)+1):
        if num%j==0:
            c = 0
            while num%j==0:
                num //= j
                c += 1
            memo[j] = max(memo[j], c)
    if num != 1:
        memo[num] = max(memo[num], 1)
k = 1
for s, t in memo.items():
    k = (k*pow(s, t, mod))%mod

print((k*base)%mod)