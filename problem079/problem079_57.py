s = int(input())
MOD = 10**9 + 7
b3 = 1; b2 = 0; now = 0 # now == b1
for n in range(3, s+1):
    b1 = now
    now = (b1 + b3) % MOD
    b3, b2 = b2, b1
print(now)
