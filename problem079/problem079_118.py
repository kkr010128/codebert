s = int(input())
MOD = 10**9 + 7
b3 = 1; b2 = 0; now = 0 # now == b1
for _ in range(s-2):
    b1 = now
    now = (b1 + b3) % MOD
    b3, b2 = b2, b1
print(now)
