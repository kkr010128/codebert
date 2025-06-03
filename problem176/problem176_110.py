MOD = 1000000007
def mod_pow(x , y):
    if y == 0:
        return 1
    if y == 1:
        return x
    r = mod_pow(x , y // 2)
    r2 = (r * r) % MOD
    if y % 2 == 0:
        return r2 % MOD
    else:
        return (r2 * x) % MOD

N , K = map(int , input().split())
result = 0
memo = {}
for g in range(K , 0 , -1):
    comb = mod_pow(K // g , N)
    for j in range(2 , K // g + 1):
        comb = (comb - memo[j * g] + MOD) % MOD
    memo[g] = comb
    result = (result + comb * g) % MOD
print(result)

