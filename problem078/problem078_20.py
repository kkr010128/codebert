n = int(input())
MOD = int(1e9 + 7)

a, b, c = 1, 1, 1

for i in range(n):
    a *= 10;
    b *= 9;
    c *= 8;
    a %= MOD;
    b %= MOD;
    c %= MOD;
    
print((a - 2 * b + c) % MOD);