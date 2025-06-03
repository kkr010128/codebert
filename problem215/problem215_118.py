MOD = 1000000007  # type: int
 
def solve(n: int, k: int):
    fact = [1] * (n+1)
    inv_fact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1] % MOD
 
    inv_fact[-1] = pow(fact[-1], MOD-2, MOD)
    for i in range(n-1, 0, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
 
    def comb(n, r, MOD=MOD):
        return fact[n] * inv_fact[n-r] * inv_fact[r] % MOD
    
    ans = 0
    for i in range(min(k, n-1)+1):
        ans += comb(n, i) * comb(n-1, i) % MOD
        ans %= MOD
 
    return ans

n, k = list(map(int, input().split()))

print(solve(n, k))